function accion(){
    var ancla = document.getElementsByClassName("item-nav")
    for(var i = 0; i < ancla.length; i++ ){
        ancla[i].classList.toggle("hide")
    }
}
function cerrar(){
    document.getElementById("message").style.display="none";
}