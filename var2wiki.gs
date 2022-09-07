const SHORT_SHEET_NAME = "Краткая";
const LONG_SHEET_NAME = "Полная";

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


const WIKI_API_URL = "http://wikitest.rubikus.de/mw/api.php";

function colNames(sData) {
  colNames = sData[0];
  return colNames
}

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

function publishToWiki() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();

  var shortSheet = ss.getSheetByName(SHORT_SHEET_NAME);
  var shortData = shortSheet.getDataRange().getValues();
  var longSheet = ss.getSheetByName(LONG_SHEET_NAME);
  var longData = longSheet.getDataRange().getValues();

//  Logger.log(shortData[2]);
//  return;

  const [cookiesStore, response] = startCookies();

//   var url = WIKI_API_URL + "?action=query&meta=tokens&type=login&format=json";
//   var response = UrlFetchApp.fetch(url, {
//     'method' : 'GET'
//   });
//   var headers = response.getAllHeaders();
//   var cookies = headers['Set-Cookie']; 
//   if ((cookies != null) && (cookies[0].length == 1)) {
//     cookies = new Array(1);              
//     cookies[0] = headers['Set-Cookie']; 
//   }  
//   for (var i = 0; i < cookies.length; i++) {
// //    cookies[i] = cookies[i].split( ';' )[0];
//     cookiesStore.push(cookies[i].split( ';' )[0]);
//   };

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

  var url = WIKI_API_URL + "?action=query&meta=tokens&format=json";
  response = UrlFetchApp.fetch(url, {
    method: "GET",
    headers: {
      "Cookie": cookiesStore.join(';')
    }
  });
  Logger.log(response);

  var responseData = JSON.parse(response);
  var crfsToken = responseData.query.tokens.csrftoken;

  const topics = shortData[1];
  for (var row = 2; row < shortData.length; row++) {
    if (shortData[row][1] == "") continue;

    for (var col = 4; col < shortData[0].length; col++) {
      url = WIKI_API_URL + "?action=edit";
      form = {
        token: crfsToken,
        bot: true,
        title: "Template:varenik_" + shortData[row][1] + "_" + topics[col] + "_short",
        text: shortData[row][col],
        format: "json",
      }
      response = UrlFetchApp.fetch(url, {
        method: "POST",
        headers: {
          "Cookie": cookiesStore.join(';')
        },
        payload: form
      });
      Logger.log(response);
    }
  }

}