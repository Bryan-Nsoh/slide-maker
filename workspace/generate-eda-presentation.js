const pptxgen = require('pptxgenjs');
const html2pptx = require('../scripts/html2pptx');

async function createPresentation() {
    const pptx = new pptxgen();
    pptx.layout = 'LAYOUT_16x9';
    pptx.author = 'Bryan Nsoh';
    pptx.title = 'Exploratory Data Analysis - LSTM VWC Prediction';

    // Slide 1: Title
    await html2pptx('workspace/html-slides/slide-01.html', pptx);

    // Slide 2: Project Context
    await html2pptx('workspace/html-slides/slide-02.html', pptx);

    // Slide 3: Problem Statement
    await html2pptx('workspace/html-slides/slide-03.html', pptx);

    // Slide 4: Data Collection Pipeline (placeholder for image)
    await html2pptx('workspace/html-slides/slide-04.html', pptx);

    // Slide 5: Dataset Summary
    await html2pptx('workspace/html-slides/slide-05.html', pptx);

    // Slide 6: Native Data Features with table
    const { slide: slide6, placeholders: ph6 } = await html2pptx('workspace/html-slides/slide-06.html', pptx);

    const nativeFeatures = [
        [
            { text: "Feature", options: { bold: true, fill: { color: "16A085" }, color: "FFFFFF" } },
            { text: "Description", options: { bold: true, fill: { color: "16A085" }, color: "FFFFFF" } },
            { text: "Units", options: { bold: true, fill: { color: "16A085" }, color: "FFFFFF" } }
        ],
        ["Ta_2m_Avg", "Air temperature at 2m", "°C"],
        ["RH_2m_Avg", "Relative humidity at 2m", "%"],
        ["Solar_2m_Avg", "Solar radiation at 2m", "W/m²"],
        ["WndAveSpd_3m", "Wind speed at 3m", "m/s"],
        ["Rain_1m_Tot", "Rainfall total at 1m", "mm"],
        ["VWC_06/18/30", "Volumetric water content (depths)", "%"],
        ["canopy_temp", "Canopy temperature", "°C"],
        ["irrigation", "Irrigation amount", "mm"],
        ["precip_irrig", "Combined precip + irrigation", "mm"]
    ];

    const featureTable = ph6.find(p => p.id === 'feature-table');
    if (featureTable) {
        slide6.addTable(nativeFeatures, {
            ...featureTable,
            fontSize: 12,
            border: { pt: 1, color: "CCCCCC" },
            align: "left",
            valign: "middle",
            colW: [2.5, 3.5, 1.5]
        });
    }

    // Slide 7: Engineered Features with table
    const { slide: slide7, placeholders: ph7 } = await html2pptx('workspace/html-slides/slide-07.html', pptx);

    const engineeredFeatures = [
        [
            { text: "Feature", options: { bold: true, fill: { color: "E67E22" }, color: "FFFFFF" } },
            { text: "Description", options: { bold: true, fill: { color: "E67E22" }, color: "FFFFFF" } },
            { text: "Purpose", options: { bold: true, fill: { color: "E67E22" }, color: "FFFFFF" } }
        ],
        ["VWC_*_spike_up", "15% increase detection", "Capture irrigation/rain events"],
        ["VWC_*_spike_down", "15% decrease detection", "Detect rapid drainage"],
        ["time_since_last_precip", "Days since last rain event", "Temporal drought indicator"],
        ["precip_cumulative_7day", "7-day rolling sum", "Water supply over window"],
        ["VWC_*_smoothed", "Savitzky-Golay filtered", "Noise reduction"],
        ["VWC_*_deriv", "Rate of change", "Capture dynamics"],
        ["precip_irrig_log", "Log-transformed precip", "Handle skewed distribution"],
        ["Cyclic time encoding", "Sin/cos of hour, day, DOW", "Capture temporal patterns"]
    ];

    const engTable = ph7.find(p => p.id === 'engineered-table');
    if (engTable) {
        slide7.addTable(engineeredFeatures, {
            ...engTable,
            fontSize: 11,
            border: { pt: 1, color: "CCCCCC" },
            align: "left",
            valign: "middle",
            colW: [2.2, 2.5, 3.3]
        });
    }

    // Slide 8: Raw VWC Data (placeholder for image)
    await html2pptx('workspace/html-slides/slide-08.html', pptx);

    // Slide 9: Domain Knowledge
    await html2pptx('workspace/html-slides/slide-09.html', pptx);

    // Slide 10: Basic Data Cleaning
    await html2pptx('workspace/html-slides/slide-10.html', pptx);

    // Slide 11: Interpolating Missing Values
    await html2pptx('workspace/html-slides/slide-11.html', pptx);

    // Slide 12: Spike Detection
    await html2pptx('workspace/html-slides/slide-12.html', pptx);

    // Slide 13: Time Since Precipitation
    await html2pptx('workspace/html-slides/slide-13.html', pptx);

    // Slide 14: Savitzky-Golay Filter
    await html2pptx('workspace/html-slides/slide-14.html', pptx);

    // Slide 15: Data Transformations
    await html2pptx('workspace/html-slides/slide-15.html', pptx);

    // Slide 16: Scaling with Buffer
    await html2pptx('workspace/html-slides/slide-16.html', pptx);

    // TODO: Slides 17-23 temporarily disabled until validation errors resolved
    // await html2pptx('workspace/html-slides/slide-17.html', pptx);
    // await html2pptx('workspace/html-slides/slide-18.html', pptx);
    // await html2pptx('workspace/html-slides/slide-19.html', pptx);
    // await html2pptx('workspace/html-slides/slide-20.html', pptx);
    // await html2pptx('workspace/html-slides/slide-21.html', pptx);
    // await html2pptx('workspace/html-slides/slide-22.html', pptx);
    // await html2pptx('workspace/html-slides/slide-23.html', pptx);

    // Save
    await pptx.writeFile({ fileName: 'workspace/presentations/eda-lstm-vwc-prediction.pptx' });
    console.log('✓ Presentation created: workspace/presentations/eda-lstm-vwc-prediction.pptx');
}

createPresentation().catch(console.error);
