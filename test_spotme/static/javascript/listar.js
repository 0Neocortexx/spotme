function listarMusicas() {
    $.ajax({
        url: 'http://localhost:5000/listar',
        method: 'GET',
        dataType: 'json', // os dados são recebidos no formato json
        success: listar, // chama a função listar para processar o resultado
        error: anyError
    });


    function anyError() {
        alert("erro ao ler dados, verifique o backend");
    };

    function listar(musicas) {
            // percorrer a lista de pessoas retornadas; 
            for (var i in musicas) { //i vale a posição no vetor
                lin = '<tr class="table">' + // elabora linha com os dados da pessoa
                    '<td class="table-item">' + musicas[i].generos_id + '</td>' +
                    '<td class="table-item">' + musicas[i].nome + '</td>' +
                    '<td class="table-item">' + musicas[i].artista + '</td>' +
                    '<td class="table-item">' + musicas[i].link + '</td>' +
                    '</tr>';
                // adiciona a linha no corpo da tabela
                $('#corpoMusicas').append(lin);
            }
        }
}