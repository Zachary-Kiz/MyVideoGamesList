const createUser = async (data) => {
    const url = import.meta.env.VITE_API_URL + '/api/user/register'
    await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',  // Specify content type as JSON
        },
        body: JSON.stringify(data)  // Convert the data to JSON and send it in the body
    })
    .then(response => {
        if (response.ok) {
            return response.status;  // Parse the JSON response if successful
        } else {
            throw new Error('Request failed');
        }
    })
    .catch(error => {
        console.error('Error:', error);  // Handle any errors
    });

}

export default createUser;