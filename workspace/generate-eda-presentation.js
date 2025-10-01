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

    await html2pptx('workspace/html-slides/slide-06.html', pptx);

    await html2pptx('workspace/html-slides/slide-07.html', pptx);

    await html2pptx('workspace/html-slides/slide-08.html', pptx);

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

    await html2pptx('workspace/html-slides/slide-17.html', pptx);

    await html2pptx('workspace/html-slides/slide-18.html', pptx);

    await html2pptx('workspace/html-slides/slide-19.html', pptx);

    await html2pptx('workspace/html-slides/slide-20.html', pptx);

    await html2pptx('workspace/html-slides/slide-21.html', pptx);

    await html2pptx('workspace/html-slides/slide-22.html', pptx);

    await html2pptx('workspace/html-slides/slide-23.html', pptx);

    // Save
    await pptx.writeFile({ fileName: 'workspace/presentations/eda-lstm-vwc-prediction.pptx' });
    console.log('✓ Presentation created: workspace/presentations/eda-lstm-vwc-prediction.pptx');
}

createPresentation().catch(console.error);
