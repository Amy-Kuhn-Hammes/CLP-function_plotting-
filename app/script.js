let idCount = -1
document.querySelector("#min").value = -10
document.querySelector("#max").value = 10


document.querySelector("#btn").addEventListener('click', () => {
    
    idCount++;
    document.querySelector("#inputs").innerHTML += 
        `<div  id = "div${idCount}" style="display: flex">
            <h2 id = "${idCount}">Y = &nbsp</h2> 
            <input id = "input${idCount}"></input>
            <button class="buttonDelete" onClick="deleteInput(${idCount})"id ="${idCount}">X</button> 
        </div>`
}) 

function deleteInput(id) {
    document.querySelector("#div"+id).innerHTML = ' '
}

function submitForm() {
    const xhttp = new XMLHttpRequest();
    const funcArr = []

    for(let i = 0; i <= idCount; i++) {
        try {
            funcArr.push(document.querySelector("#input"+i).value) 
        } catch {
            continue
        }
    }
    
    xhttp.onload = function() {
        document.querySelector("#img").src = 'data:image;base64, '+this.responseText
    }
    xhttp.open("POST", "http://127.0.0.1:5000/plot", true);
    xhttp.setRequestHeader('Content-Type', 'application/json')
    xhttp.send(JSON.stringify({
        min: -10,
        max: 10,
        funcs: funcArr
    }));    
}

