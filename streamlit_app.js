async function query(data) {
    const response = await fetch(
        "https://tomas3254-legalbot.hf.space/api/v1/prediction/b21709c5-f495-4db2-9ca5-9f6129441557",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );
    const result = await response.json();
    return result;
}

query({"question": "Hey, how are you?"}).then((response) => {
    console.log(response);
});
