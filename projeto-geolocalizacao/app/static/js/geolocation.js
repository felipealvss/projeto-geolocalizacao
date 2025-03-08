// Função para obter a localização do usuário
function getLocation() {
    if (navigator.geolocation) {
        // Solicita a posição atual do usuário
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        // Exibe mensagem se a geolocalização não for suportada
        document.getElementById("location").innerHTML = "Geolocalização não suportada.";
    }
}

// Função para exibir a posição do usuário
function showPosition(position) {
    let now = new Date();
    let dateTime = now.toLocaleString("pt-BR");
    
    let latitude = position.coords.latitude;
    let longitude = position.coords.longitude;

    // Exibe a data, latitude e longitude na página
    document.getElementById("location").innerHTML =
        `<strong>Data verificação:</strong> ${dateTime}<br>
         <strong>Latitude:</strong> ${latitude}<br>
         <strong>Longitude:</strong> ${longitude}`;

    // Envia os dados de localização para o backend
    fetch('/log', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ latitude, longitude })
    })
    .then(response => response.json())
    .then(data => console.log(data.message))
    .catch(error => console.error('Erro ao enviar dados:', error));
}

// Função para exibir erros de geolocalização
function showError(error) {
    let now = new Date();
    let dateTime = now.toLocaleString("pt-BR");

    let message = `<strong>Data verificação:</strong> ${dateTime}<br>`;

    // Define a mensagem de erro com base no código de erro
    switch(error.code) {
        case error.PERMISSION_DENIED:
            message += "Usuário negou a solicitação de geolocalização.";
            break;
        case error.POSITION_UNAVAILABLE:
            message += "Informação de localização indisponível.";
            break;
        case error.TIMEOUT:
            message += "A solicitação expirou.";
            break;
        case error.UNKNOWN_ERROR:
            message += "Ocorreu um erro desconhecido.";
            break;
    }
    // Exibe a mensagem de erro na página
    document.getElementById("location").innerHTML = message;
}