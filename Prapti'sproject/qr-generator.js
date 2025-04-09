// qr-generator.js

function generateQRCode(totalAmount) {
    const qrContainer = document.getElementById("qr-container");
  
    // Clear any existing QR code
    qrContainer.innerHTML = "";
  
    // Generate the QR code
    const qrCode = new QRCode(qrContainer, {
      text: `https://example.com/payment?amount=${totalAmount}`,
      width: 128,
      height: 128,
    });
  
    const totalPriceElem = document.createElement("div");
    totalPriceElem.classList.add("total-price");
    totalPriceElem.textContent = `Total: ₹${totalAmount}`;
  
    qrContainer.appendChild(totalPriceElem);
  }
  
