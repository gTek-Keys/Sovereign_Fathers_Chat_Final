document.getElementById('generateContract').addEventListener('click', () => {
    const address = document.getElementById('propAddress').value;
    const desc = document.getElementById('propDesc').value;
    const img = document.getElementById('propImg').value;
    const owner = document.getElementById('ownerWallet').value;
    const price = document.getElementById('price').value;

    const contract = {
        property: { address, desc, img },
        sale: { owner, price }
    };

    document.getElementById('output').textContent =
        'Generated Contract:\n' + JSON.stringify(contract, null, 2);
});

document.getElementById('mintNft').addEventListener('click', () => {
    const output = document.getElementById('output');
    output.textContent += '\n\n[Placeholder] Minting transaction submitted...';
});
