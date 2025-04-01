document.getElementById('clear-button').addEventListener('click', function() {
    clearExperiences();
});


function addProduct() {
    let title = document.getElementById('title').value
    let link = document.getElementById('link').value
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'title': title,
                             'link': link})
    })

function addProduct() {
    fetch('/clear', {method: 'post'}).then(response => response.json()).then(data => {
        const ProjectsList = document.getElementById('id');
        ProjectsList.innerHTML = '';
        console.log(data.message))})
    }
}