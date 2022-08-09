// this function is what is triggered by the form
// function sendData(form)  {
//     const XHR = new XMLHttpRequest();
//     const FD = new FormData();

//     // what happens on successful submit
//     XHR.addEventListener("load", function(event) {
//	// TODO
//     });

//     XHR.addEventListener( "error", function(event) {
//	// TODO
//     });

//     XHR.open( "POST", "{{ APP_URL}}/update");
// }

// $(document).ready(function(){
//     $.ajax({

//     })
// })

function addDataToSend(event) {

    event.preventDefault()
    submitter = event.submitter;
    form = submitter.parentNode;
    console.log(parent)

    inputs = form.getElementsByClassName("fauxinput")
    tags = form.getElementsByClassName("tag")
    for (let i = 0; i < inputs.length; i++) {
	let input = inputs[i];
	classname = input.className
	actualclass = classname.substring(10)

	var hidden = document.createElement("input")
	hidden.type = "hidden";
	hidden.name = actualclass;
	hidden.value = input.innerHTML;
	form.appendChild(hidden)


	console.log(actualclass)
	console.log(input.innerHTML)
    }
    form.submit()

}

const theseforms = document.querySelectorAll("form");
// var forms = $("form");
console.log("# forms: " + theseforms.length)

for (let i = 0; i < theseforms.length; i++) {
    let form = theseforms[i];
    form.addEventListener('submit', addDataToSend, true)
}

// for (const form in theseforms) {
//     // form.addEventListener('submit', addDataToSend)
//     console.log(form)
// }
