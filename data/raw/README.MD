# Raw Data Directory

## Overview

This directory contains unprocessed, original data files. These files should remain unchanged to maintain data integrity and provide a source of truth.

## Directory Contents

- Survey responses
- System logs
- Customer feedback
- Raw metrics
- External datasets

## File Naming Convention

Format: `YYYY-MM-DD_data-type_source.extension`
Example: `2024-11-17_survey-responses_web.csv`

## Data Sources

- Customer Surveys (\*.csv)
- System Analytics (\*.json)
- User Feedback Forms (\*.xlsx)
- External Reports (\*.pdf)

## Guidelines

1. Never modify raw data files
2. Document data sources
3. Include data collection date
4. Maintain original file formats

## Metadata Requirements

Each dataset should include:

- Collection date
- Source
- Format specifications
- Contact person
- Version/batch number

## Access Permissions

- Read-only access for team members
- Write access restricted to data engineers
- Backup performed daily
