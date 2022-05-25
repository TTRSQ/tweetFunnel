const url = "your cloud function url";

function runTweet() {

    let sheet = SpreadsheetApp.getActiveSheet();
    let lastRow = sheet.getLastRow();
    var values = sheet.getRange(lastRow, 1, 1, 3).getValues();
    console.log(values[0][0])

    let content = values[0][0]

    var headers = {
        "Content-Type": "application/json"
    };
    var options = {
        "headers": headers,
        "method": "post",
        "payload": JSON.stringify({ "text": content }),
    };
    let res = UrlFetchApp.fetch(url, options).getContentText('UTF-8');

    console.log(res);
}
