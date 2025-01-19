```1. explain the csrf_token: security code```
var csrf_token = "{{ csrf_token }}"

```2. select the object```
/* define the elements as variables  */
var mean_input = document.querySelector(".mean_input")
var std_input = document.querySelector(".std_input")
var sample_number_input = document.querySelector(".sample_number_input")
var submit_button = document.querySelector(".submit")
var img_object = document.querySelector(".graph")

```3. print the selected object```
console.log(mean_input)
console.log(submit_button)
console.log(img_object)


```4. print the input values```
console.log(mean_input.value)
console.log(submit_button.value)
console.log(img_object.value)


```5. click function```
submit_button.addEventListener("click", function(){
    console.log("the button is clicked.")
})


```6. get the value of the inputs, but they are strings```
submit_button.addEventListener("click", function(){
    var input_json = {
        "mean": mean_input.value,
        "std": std_input.value,
        "N": sample_number_input.value
    }

    console.log(input_json)
})

```7. get the value of the inputs and convert them into floats and integers```
submit_button.addEventListener("click", function(){
    var input_json = {
        "mean": parseFloat(mean_input.value),
        "std": parseFloat(std_input.value),
        "N": parseInt(sample_number_input.value)
    }

    console.log(input_json)
})

```8. XMLHttpRequest object```
const xhttp = new XMLHttpRequest();
var url = 'graph_generator';
xhttp.open('POST', url, true);
xhttp.setRequestHeader("X-CSRFToken", csrf_token);
xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

xhttp.onreadystatechange = function() {//Call a function when the state changes.
    if(xhttp.readyState == 4 && xhttp.status == 200) {

    }
}

xhttp.send(JSON.stringify(input_json));

```9. response function```
xhttp.onreadystatechange = function() {//Call a function when the state changes.
     if(xhttp.readyState == 4 && xhttp.status == 200) {
         var returnData = JSON.parse(xhttp.responseText)
         console.log("return data = ", returnData)
         img_object.src = "/static/" + returnData["imgSrc"]
     }
 }
