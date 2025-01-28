/* Called in the profiles/manage.html file when a user wants to remove a game from their library */
function confirmRemove(gameId, gameName) {
    document.getElementById('remove_game_id').value = gameId;
    document.getElementById('gameName').textContent = gameName;
    document.getElementById('confirmRemoveModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('confirmRemoveModal').style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function() {
    var closeButtons = document.querySelectorAll('.close, .btn-secondary');
    closeButtons.forEach(function(button) {
        button.addEventListener('click', closeModal);
    });
});