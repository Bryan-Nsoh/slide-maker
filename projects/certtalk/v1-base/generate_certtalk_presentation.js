#!/usr/bin/env node
/**
 * Generate CertTalk presentation from HTML slides using html2pptx.
 *
 * This script converts 6 HTML slides into a PowerPoint presentation following
 * the html2pptx workflow documented in docs/html2pptx.md.
 */

const pptxgen = require('pptxgenjs');
const html2pptx = require('./scripts/html2pptx.js');
const path = require('path');

async function generatePresentation() {
  console.log('CertTalk Presentation Generator');
  console.log('================================\n');

  // Create presentation
  const pptx = new pptxgen();
  pptx.layout = 'LAYOUT_16x9';
  pptx.author = 'CertTalk Team';
  pptx.title = 'CertTalk: Approach & Experiments';
  pptx.subject = 'Multi-agent communication with certificates';

  const slideFiles = [
    'workspace/html-slides/slide1.html',
    'workspace/html-slides/slide2.html',
    'workspace/html-slides/slide4.html',
    'workspace/html-slides/slide5.html',
    'workspace/html-slides/slide6.html',
    'workspace/html-slides/slide7.html'
  ];

  const slideNames = [
    'The Problem',
    'The Solution - Certificates',
    'What We\'ll Compare',
    'How We\'ll Test',
    'Our Approach',
    'Timeline & Deliverables'
  ];

  // Convert each HTML slide
  for (let i = 0; i < slideFiles.length; i++) {
    const htmlFile = slideFiles[i];
    const slideName = slideNames[i];

    console.log(`[${i + 1}/${slideFiles.length}] Processing: ${slideName}...`);

    try {
      const { slide, placeholders } = await html2pptx(htmlFile, pptx);

      if (placeholders.length > 0) {
        console.log(`  → Found ${placeholders.length} placeholder(s)`);
      }

      console.log(`  ✓ Slide ${i + 1} created successfully`);
    } catch (error) {
      console.error(`  ✗ Error processing ${htmlFile}:`, error.message);
      throw error;
    }
  }

  // Save presentation
  const outputFile = 'CertTalk_Presentation.pptx';
  console.log(`\nSaving presentation to: ${outputFile}`);

  await pptx.writeFile({ fileName: outputFile });

  console.log('\n✓ Presentation generated successfully!');
  console.log(`✓ Total slides: ${pptx.slides.length}`);
  console.log(`\nNext steps:`);
  console.log(`  1. Open: open ${outputFile}`);
  console.log(`  2. Validate: python scripts/thumbnail.py ${outputFile}`);
}

// Run generator
generatePresentation().catch(error => {
  console.error('\n✗ Error generating presentation:', error);
  process.exit(1);
});
