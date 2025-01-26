function confirmRemove(gameId) {
    document.getElementById('remove_game_id').value = gameId;
    $('#confirmRemoveModal').modal('show');
}