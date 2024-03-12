// function deleteNote(noteId) {
//     // fetch('/delete-note', {
//     //     method: 'POST',
//     //     body: JSON.stringify({ noteId: noteId }),
//     // }).then((_res) => {
//     //     window.location.href = '/';
//     // });
// }

function myFunction() {
    if (confirm("Are you sure to log out?")) {
        window.location.href = '/logout';
    }
  }