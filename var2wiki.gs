const SHORT_SHEET_NAME = "Краткая";
const LONG_SHEET_NAME = "Полная";
// const UPLOAD_URL = "";

function publishData() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  // console.log(UPLOAD_URL);

  var shortSheet = ss.getSheetByName(SHORT_SHEET_NAME);
  var shortData = shortSheet.getDataRange().getValues();
  var longSheet = ss.getSheetByName(LONG_SHEET_NAME);
  var longData = longSheet.getDataRange().getValues();

  var data = {
    version: 1,
    updateDate: new Date(),
    columnsToShow: [
      "documents",
      "statuses",
      "payments",
      "housing",
      "medicine",
      "transport",
      "work",
      "education",
      "driver",
      "pets",
      "covid"
    ],
    dataShort: shortData,
    dataLong: longData
  }

  var payload = JSON.stringify(data);
  var response = UrlFetchApp.fetch(UPLOAD_URL, {
    'method' : 'PUT',
    'contentType' : "application/json",
    'payload' : payload
  });
}

function onOpen() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet();
  var entries = [
    { name : "опубликовать", functionName : "publishData"},
  ];
  sheet.addMenu("Вареник", entries);
};

// === To Wiki ===
const WIKI_API_URL = "http://wikitest.rubikus.de/mw/api.php";

function startCookies() {
  var cookiesStore = [];

  var url = WIKI_API_URL + "?action=query&meta=tokens&type=login&format=json";
  var response = UrlFetchApp.fetch(url, {
    'method' : 'GET'
  });
  var headers = response.getAllHeaders();
  var cookies = headers['Set-Cookie']; 
  if ((cookies != null) && (cookies[0].length == 1)) {
    cookies = new Array(1);              
    cookies[0] = headers['Set-Cookie']; 
  }  
  for (var i = 0; i < cookies.length; i++) {
//    cookies[i] = cookies[i].split( ';' )[0];
    cookiesStore.push(cookies[i].split( ';' )[0]);
  };

  return [cookiesStore, response]
}

function login2Wiki(cookiesStore, response) {
  var responseData = JSON.parse(response);
  var loginToken = responseData.query.tokens.logintoken;
  Logger.log(loginToken);

  url = WIKI_API_URL + "?action=login";
  var form = {
    lgname: "",
    lgpassword: "",
    lgtoken: loginToken,
    format: "json"
  }
  response = UrlFetchApp.fetch(url, {
    method: "POST",
    headers: {
      "Cookie": cookiesStore.join(';')
    },
    payload: form
  });
  var headers = response.getAllHeaders();
  var cookies = headers['Set-Cookie']; 
  if ((cookies != null) && (cookies[0].length == 1)) {
        cookies = new Array(1);              
        cookies[0] = headers['Set-Cookie']; 
  }  
  for (var i = 0; i < cookies.length; i++) {
//    cookies[i] = cookies[i].split( ';' )[0];
    cookiesStore.push(cookies[i].split( ';' )[0]);
  };
  Logger.log(response);
}

function getToken(cookiesStore) {
  var url = WIKI_API_URL + "?action=query&meta=tokens&format=json";
  response1 = UrlFetchApp.fetch(url, {
    method: "GET",
    headers: {
      "Cookie": cookiesStore.join(';')
    }
  });
  Logger.log(response1);

  var responseData = JSON.parse(response1);
  var crfsToken = responseData.query.tokens.csrftoken;
  return crfsToken;
}

function publishToWiki() {
  const startTime = Date.now();

  // var ss = SpreadsheetApp.getActiveSpreadsheet();
  var ss = SpreadsheetApp.openById("");

  var shortSheet = ss.getSheetByName(SHORT_SHEET_NAME);
  var shortData = shortSheet.getDataRange().getValues();
  var longSheet = ss.getSheetByName(LONG_SHEET_NAME);
  var longData = longSheet.getDataRange().getValues();

//  Logger.log(shortData[2]);
//  return;

  const [cookiesStore, response0] = startCookies();
  login2Wiki(cookiesStore, response0);
  crfsToken = getToken(cookiesStore);

  var myData = longData;
  var myPostfix = "long"
  var myDivider = "-";
  var colNames = myData[1];
  for (var row = 2; row < myData.length; row++) {
    if (myData[row][1] == "") continue;
    var countryName = myData[row][1]
    // Logger.log(countryName);

    for (var col = 4; col < myData[0].length; col++) {
      // Logger.log(myData[row][col]);
      var topic = colNames[col];
      if (topic == "") { continue; } // skip an empty column header
      // Logger.log(topic);
      var content = myData[row][col] + "\n\n[[Category:Varenik]]"
      var pageName = "Varenik" + myDivider + countryName + myDivider + topic + myDivider + myPostfix
      // Logger.log(pageName);
      url = WIKI_API_URL + "?action=edit";
      form = {
        token: crfsToken,
        bot: true,
        title: pageName,
        text: content,
        format: "json",
      }
      response2 = UrlFetchApp.fetch(url, {
        method: "POST",
        headers: {
          "Cookie": cookiesStore.join(';')
        },
        payload: form
      });
      // Logger.log(response2);
    }
  }
  const endTime = Date.now();
  var diffTime = endTime - startTime
  Logger.log(diffTime);
}
