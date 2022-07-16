// alert("hi");

// api url
const article_api_url = "https://2nugwu.deta.dev/article/";
// const article_api_url = "http://127.0.0.1:8000/article/";
const api_url = "https://2nugwu.deta.dev/";

const options = {
  method: 'GET',
  mode: "cors",
  // credentials: 'omit',
	headers: {
    "content-type": "application/json",
    "Access-Control-Allow-Origin": "*",
	}
};

fetch(api_url, options)
  .then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("NETWORK RESPONSE ERROR");
    }
  })
  .then(data => {
    console.log(data);
    displayWelcome(data)
  })
  .catch((error) => console.error("FETCH ERROR:", error));

  function displayWelcome(data) {

    const welcomeMessage = data;
    const welcomeDiv = document.getElementById("welcome");    
  
    // date name
    const welcomeMessageMessage = welcomeMessage.message;
    const heading = document.createElement("h2");
    heading.innerHTML = "Message: " + welcomeMessageMessage;
    welcomeDiv.appendChild(heading);
  
  }

  function displayInput() {

    const Input1 = document.getElementById('formGroupExampleInput').value;
    const Input1Div = document.getElementById("input1");    
  
    // date name
    // const welcomeMessageMessage = Input1;
    const heading = document.createElement("h4");
    heading.innerHTML = "Input: " + Input1;
    Input1Div.appendChild(heading);
  
  }

  displayInput();

let jsonObj = {"content": "please James, wants 2000"}
let postHeaders = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }

async function makePostRequest(url, requestType, postHeaders, jsonObj){
    await fetch(
      url,
        {
            method: requestType,
            headers: postHeaders,
            body: JSON.stringify(jsonObj)
        },
    ).then(async rawResponse =>{
        var content = await rawResponse.json()
        console.log(content);
    });
}

makePostRequest(article_api_url, "POST", postHeaders, jsonObj);