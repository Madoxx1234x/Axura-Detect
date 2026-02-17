// -----------------------------
// Redirect new users
// -----------------------------
if (!localStorage.getItem("visited")) {
  window.location.href = "welcome.html";
}

// -----------------------------
// Deep Learning Required Fields
// -----------------------------
// API base URL. Set `window.BACKEND_URL` in the page to override.
const BASE = window.BACKEND_URL || "http://127.0.0.1:5000";

const fields = {
  wildfire: ["temperature", "humidity", "wind_speed", "forest_size"],
  tornado: ["wind_shear", "pressure", "temp_gradient"],
  flood: ["rainfall", "river_level", "terrain_slope"],
  earthquake: ["magnitude", "depth", "historical_events"],
};

// -----------------------------
// Loading Spinner & Risk Meter
// -----------------------------
function showLoading() {
  const screen = document.getElementById("screen");
  screen.innerHTML = '<div class="spinner"></div>';
  document.getElementById("robotText").innerText = "Analyzing...";
}

function updateRiskBar(risk) {
  let meter = document.getElementById("riskMeter");
  if (!meter) {
    meter = document.createElement("div");
    meter.id = "riskMeter";
    meter.className = "risk-bar-container";
    const bar = document.createElement("div");
    bar.className = "risk-bar";
    meter.appendChild(bar);
    document.querySelector(".robot-card").appendChild(meter);
  }
  meter.querySelector(".risk-bar").style.width = `${risk * 100}%`;
  if (risk > 0.6)
    meter.querySelector(".risk-bar").style.background = "var(--danger)";
  else if (risk > 0.3)
    meter.querySelector(".risk-bar").style.background = "yellow";
  else meter.querySelector(".risk-bar").style.background = "var(--safe)";
}

// -----------------------------
// Generate Input Form
// -----------------------------
function selectDisaster(type) {
  document.getElementById("screen").innerHTML = '<div class="spinner"></div>';
  document.getElementById("robotText").innerText =
    "Enter the required values and analyze.";

  let html = `<h3>${type.toUpperCase()}</h3>`;

  fields[type].forEach((f) => {
    html += `<input id="${f}" placeholder="${f}" required /><br>`;
  });

  html += `<button onclick="analyze('${type}')">Analyze</button>`;

  document.getElementById("form").innerHTML = html;
}

// -----------------------------
// Analyze & Connect to Backend
// -----------------------------
async function analyze(type) {
  const data = {};
  fields[type].forEach((f) => {
    data[f] = Number(document.getElementById(f).value);
  });

  showLoading();
  updateRiskBar(0);

  // keep the loading spinner visible for 3 seconds before contacting backend
  await new Promise((resolve) => setTimeout(resolve, 3000));

  try {
    const res = await fetch(`${BASE}/predict/${type}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    const result = await res.json();
    const risk = result.risk_score || result.risk || 0;

    updateRiskBar(risk);

    // Risk face mapping:
    // - Low (<= 30%): =]
    // - Moderate (> 30% and <= 90%): =/
    // - Very high (> 90%): =[
    let screenIcon = "=]";
    let text = `Low ${type} risk. (${(risk * 100).toFixed(1)}%)`;
    if (risk > 0.9) {
      screenIcon = "=[";
      text = `High ${type} risk! (${(risk * 100).toFixed(1)}%)`;
    } else if (risk > 0.3) {
      screenIcon = "=/";
      text = `Moderate ${type} risk. (${(risk * 100).toFixed(1)}%)`;
    }

    document.getElementById("screen").innerText = screenIcon;
    document.getElementById("robotText").innerText = text;

    addHistory(`${type.toUpperCase()} → ${(risk * 100).toFixed(1)}% risk`);
  } catch (error) {
    console.error(error);
    document.getElementById("screen").innerText = "=]";
    document.getElementById("robotText").innerText = "Backend not responding!";
  }
}

// -----------------------------
// History System
// -----------------------------
function addHistory(text) {
  const li = document.createElement("li");
  li.textContent = text;
  document.getElementById("historyList").prepend(li);
}
// -----------------------------
// History System with localStorage
// -----------------------------

// Load history on page load
function loadHistory() {
  const savedHistory = JSON.parse(localStorage.getItem("recentChecks")) || [];
  const historyList = document.getElementById("historyList");
  historyList.innerHTML = ""; // clear first
  savedHistory.forEach((text) => {
    const li = document.createElement("li");
    li.textContent = text;
    historyList.appendChild(li);
  });
}

// Add new check to history
function addHistory(text) {
  const historyList = document.getElementById("historyList");

  // Add to DOM
  const li = document.createElement("li");
  li.textContent = text;
  historyList.prepend(li);

  // Save to localStorage
  const savedHistory = JSON.parse(localStorage.getItem("recentChecks")) || [];
  savedHistory.unshift(text); // newest first
  localStorage.setItem("recentChecks", JSON.stringify(savedHistory));
}
