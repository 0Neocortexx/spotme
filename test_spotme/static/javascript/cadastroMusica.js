function cadastrarMusica() {
    nomeMusica = document.getElementById('nome').value;
    artistaMusica = document.getElementById('artista').value;
    linkMusica = document.getElementById('link').value;
    generoSelect = document.getElementById('genero');
    
    idGenero = generoSelect.options[generoSelect.selectedIndex].id;
    console.log(idGenero)

    data = JSON.stringify({generos_id: idGenero, nome: nomeMusica, artista: artistaMusica, link: linkMusica})

    $.ajax({
        url: 'http://localhost:5000/inserir',
        type: 'POST', // TESTE COM A OPÇÃO GET no front e no back; observe o log do servidor
        dataType: 'json', // os dados são recebidos no formato json
        data: data, // estes são os dados enviados
        success: anySuccess,
        error: anyError
    })

    function anyError(retorno) {
        // informar mensagem de erro
        alert("ERRO ao contactar back-end: "+retorno.resultado + ":" + retorno.detalhes);
    }

    function anySuccess(retorno){
        if (retorno.resultado == "ok") { // a operação deu certo?
            // informar resultado de sucesso
            alert("Musica incluida com sucesso!");
        } else {
            // informar mensagem de erro
            alert("ERRO na inclusão: "+retorno.resultado + ":" + retorno.detalhes);
        }}  
        
        
}