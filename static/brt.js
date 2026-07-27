
function handleRegister(select) {
    const url = select.value;
    if (url) {
        window.location.href = url; 
    }
}

function handleLogin(select) {
    const url = select.value;
    if (url) {
        window.location.href = url;
    }
}
document.getElementById("startBtn").addEventListener("click", function(){
    fetch("/start_test")
    .then(res => res.text())
    .then(data => {
        window.location.href = "/informtion";
    })
});