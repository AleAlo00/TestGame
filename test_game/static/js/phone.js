// Recupera il colore dal localStorage o dalle caratteristiche del telefono
let currentColor;
    
// Controlla se il colore è presente nel localStorage per questo telefono
const phoneId = {{ myphone.id|safe }}; // Usa l'ID del telefono come chiave unica
const storedColor = localStorage.getItem(`phoneColor_${phoneId}`);

if (storedColor) {
  currentColor = storedColor; // Colore salvato in precedenza
} else if ("Color" in {{ myphone.characteristics|safe }} && "{{ myphone.characteristics.Color|default:'' }}") {
  currentColor = "{{ myphone.characteristics.Color|default:'' }}".toLowerCase(); // Colore dalla caratteristica
} else {
  currentColor = "gray"; // Colore di default
}

// Imposta il colore iniziale del telefono
const phoneImage = document.getElementById("phone-image");
phoneImage.style.backgroundColor = currentColor;

// Recupera gli elementi del DOM per caratteristiche e specifiche
const characteristics = {{ default_characteristics|safe }};
const characteristicSelect = document.getElementById("characteristic");
const specificSelect = document.getElementById("specific");

// Aggiungi una mappa dei loghi
const logoMap = {
  "Samsung": "/static/logos/samsung.png",
  "Apple": "/static/logos/apple.png",
  "Huawei": "/static/logos/huawei.png",
  "Xiaomi": "/static/logos/xiaomi.png",
  "Oppo": "/static/logos/oppo.png"
};

// Aggiorna la visualizzazione del logo in base al brand
const logoImg = document.getElementById("logo-img");

// Inizializza il logo del brand
function updateLogo(brand) {
  if (brand && logoMap[brand]) {
    logoImg.src = logoMap[brand]; // Aggiorna il logo con il path dell'immagine
  } else {
    logoImg.src = ""; // Nessun logo disponibile
  }
}

// Mostra il logo del brand iniziale
const initialBrand = "{{ myphone.characteristics.Brand|default:'' }}";
updateLogo(initialBrand);

// Aggiorna le opzioni specifiche in base alla caratteristica selezionata
characteristicSelect.addEventListener("change", function () {
  const selectedCharacteristic = characteristicSelect.value;

  // Pulisce la lista delle specifiche
  specificSelect.innerHTML = '<option value="">Select a specific</option>';

  if (selectedCharacteristic && characteristics[selectedCharacteristic]) {
    const specifics = characteristics[selectedCharacteristic];
    specifics.forEach(function (spec) {
      const option = document.createElement("option");
      option.value = spec;
      option.textContent = spec;
      specificSelect.appendChild(option);
    });
  }

  // Se la caratteristica è "Camera", ruota il telefono per mostrare il retro
  if (selectedCharacteristic === "Numero Camera") {
    rotatePhone(); // Gira il telefono sul retro
  }
});

// Gestisce la modifica delle specifiche
specificSelect.addEventListener("change", function () {
  const selectedSpecific = specificSelect.value;

  if (selectedSpecific && characteristicSelect.value === "Color") {
    const color = selectedSpecific.toLowerCase(); // Colore scelto
    phoneImage.style.backgroundColor = color; // Aggiorna il colore in tempo reale
    localStorage.setItem(`phoneColor_${phoneId}`, color); // Salva il colore nel localStorage con l'ID del telefono
    currentColor = color; // Aggiorna la variabile del colore attuale
  } else {
    // Mantieni il colore attuale se la specifica non è il colore
    phoneImage.style.backgroundColor = currentColor;
  }

  // Aggiorna il logo se la specifica riguarda il brand
  if (selectedSpecific && characteristicSelect.value === "Brand") {
    const brand = selectedSpecific; // Brand scelto
    updateLogo(brand); // Modifica il logo del brand
  }
});

// Funzione per girare il telefono
let isFront = true; // Variabile per tracciare lo stato attuale (fronte o retro)

function rotatePhone() {
  const frontElement = document.getElementById("phone-front");
  const backElement = document.getElementById("phone-back");

  if (isFront) {
    frontElement.style.display = "none";
    backElement.style.display = "block";
  } else {
    frontElement.style.display = "block";
    backElement.style.display = "none";
  }

  isFront = !isFront; // Cambia lo stato
}