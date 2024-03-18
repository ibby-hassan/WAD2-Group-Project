function vote(vote){
    
}

// document.getElementById('upvote-form').addEventListener('submit', function(event) {
//     event.preventDefault();

//     var userAuthenticated = {{ user_authenticated|yesno:"true,false" }};
//     if (!userAuthenticated) {
//         alert('Not logged in');
//         window.location.href = "{% url 'insQuire:login' %}";
//     } else {
//         var formData = new FormData(this);
//         fetch(this.action, {
//             method: 'POST',
//             body: formData,
//             headers: {
//                 'X-CSRFToken': '{{ csrf_token }}'
//             },
//             credentials: 'same-origin'
//         }).then(function(response) {
//             if (response.ok) {
//                 // Handle successful response
//             } else {
//                 // Handle error
//             }
//         });
//     }
// });