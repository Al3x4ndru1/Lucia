

function sendForm(){
  const flower = document.getElementByID("flowers").value;
  const nrflowers = document.getElementByID("nrflowers").value;
  const type = document.getElementByID("type").value;

  const dist_value = {flower, nrflowers, type}
  const s = JSON.stringify(dist_value);
  console.log(s);
  window.alert(s)
         $.ajax({
            url:"/test",
            type:"POST",
            contentType: "application/json",
            data: JSON.stringify(s)});

}

}