# VNG Data Analyzer

A modern, professional Streamlit application for analyzing and comparing VNG (Videonystagmography) test reports. Compare multiple VNG reports, track changes over time, visualize trends with advanced charts, and get AI-powered clinical interpretations.

## ✨ Features

### 📊 Data Analysis
- **Multi-file Upload**: Upload and compare multiple VNG report files (.txt format)
- **Statistical Analysis**: Calculate delta, percent change, and standard deviation across reports
- **Flag Detection**: Identify metrics that were flagged as out-of-range in original reports
- **File Preview**: Preview file contents before analysis
- **File Management**: View file metadata, validation status, and preview contents

### 📈 Advanced Visualizations

#### Chart Types
- **Line Charts**: Individual metric trends with flagged value indicators, trendlines, and optional confidence intervals
- **Category Comparison Charts**: Clustered bar charts with options for:
  - Horizontal or vertical orientation
  - Stacked bars
  - Color gradients based on change magnitude
- **Heatmap**: Visualize all metrics across all files in a color-coded grid
- **Radar/Spider Charts**: Compare multiple metrics across files simultaneously
- **Box Plots**: Show distribution and outliers for metrics with 3+ files
- **Correlation Matrix**: Visualize relationships between different metrics within a category
- **Multi-Metric Comparison**: Compare multiple metrics on the same chart

#### Chart Features
- Interactive zoom and pan (Plotly built-in)
- Export charts as interactive HTML
- Confidence intervals (95% CI) for 3+ files
- Automatic trendline calculation
- Flagged value annotations
- Customizable chart options

### 📋 Enhanced Data Tables
- **Search & Filter**: Search metrics by name or category
- **Column Configuration**: Optimized column widths and formatting
- **Export Options**: Download data as CSV or Excel
- **Color-Coded Indicators**: Visual flags for out-of-range values

### 🤖 AI-Powered Interpretation
- **Clinical Analysis**: Get high-level clinical interpretations using AI API
- **Web Search Integration**: AI uses web search to find normative data and test-retest reliability
- **Export Interpretation**: Download interpretation results
- **Model-Agnostic**: Works with any AI provider (configurable)

### 🎨 User Interface
- **Tab-Based Navigation**: Organized into Overview, Charts, Detailed Analysis, and AI Interpretation tabs
- **Dashboard Overview**: Summary cards showing key statistics (files, metrics, flagged items, significant changes)
- **Quick Statistics**: Visual indicators for trends and changes
- **Custom Styling**: Professional, modern UI with custom CSS
- **Responsive Design**: Optimized for different screen sizes

## 🚀 Setup

### Prerequisites

- Python 3.8 or higher
- Virtual environment (venv) already set up in the project

### Installation

1. **Activate the virtual environment:**

   On Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   venv\Scripts\activate
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   **Optional dependencies for enhanced features:**
   - `openpyxl` - For Excel export (included in requirements.txt)

3. **Configure AI API Key:**

   Create a `.streamlit` directory in the project root if it doesn't exist:
   ```bash
   mkdir -p .streamlit
   ```

   Copy the example secrets file:
   ```bash
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml
   ```

   Edit `.streamlit/secrets.toml` and add your API key:
   ```toml
   AI_API_KEY = "your-api-key-here"
   ```

   Alternatively, you can set the API key as an environment variable:
   ```bash
   export AI_API_KEY="your-api-key-here"
   ```

   **Note:** Configure the API endpoint and model in `config/settings.py` based on your AI provider.

## 🏃 Running the Application

1. **Make sure the virtual environment is activated** (see Installation step 1)

2. **Run Streamlit:**

   ```bash
   streamlit run app.py
   ```

3. **Open your browser:**

   The app will automatically open in your default browser, typically at `http://localhost:8501`

## 📖 Usage

### Basic Workflow

1. **Upload Files**: 
   - Click "Upload VNG Reports" and select one or more .txt VNG report files
   - View file metadata and preview file contents if needed

2. **Analyze**: 
   - Click "Analyze Files" to process and compare the reports
   - View the dashboard overview for quick insights

3. **Explore Results**: 
   - **Overview Tab**: See summary statistics and quick insights
   - **Charts Tab**: Select from 6 different chart types to visualize your data
   - **Detailed Analysis Tab**: Browse detailed tables with search and export options
   - **AI Interpretation Tab**: Get clinical interpretations of your findings

### Chart Types Guide

- **Line Chart**: Best for tracking individual metric trends over time
- **Category Comparison**: Compare all metrics within a category (with orientation and stacking options)
- **Radar Chart**: Compare multiple metrics across files in a polar view
- **Box Plot**: Analyze distribution and outliers (requires 3+ files)
- **Correlation Matrix**: Discover relationships between metrics in a category
- **Multi-Metric Comparison**: Compare 2-10 metrics on the same chart

### Export Options

- **Charts**: Export as interactive HTML
- **Tables**: Export as CSV or Excel (requires openpyxl)
- **AI Interpretation**: Copy or export interpretation results

## 📁 Project Structure

```
vng/
├── app.py                          # Main Streamlit application entry point
├── config.py                       # Backward-compatible config wrapper
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── ARCHITECTURE.md                 # Architecture documentation
│
├── config/                         # Configuration management
│   ├── __init__.py
│   ├── settings.py                 # Application settings (API endpoints, etc.)
│   ├── constants.py                # Application-wide constants
│   └── ui_config.py                # UI-specific configuration
│
├── domain/                         # Domain layer (business logic models)
│   ├── __init__.py
│   ├── models.py                   # Domain models (ParsedFile, MetricValue, etc.)
│   ├── enums.py                    # Domain enums (ChartType, AnalysisStatus, etc.)
│   └── exceptions.py               # Custom exception hierarchy
│
├── services/                       # Service layer (business logic)
│   ├── __init__.py
│   ├── file_service.py             # File handling operations
│   ├── parsing_service.py          # VNG text file parsing
│   ├── analysis_service.py         # Statistical analysis
│   ├── visualization_service.py    # Chart generation
│   └── ai_service.py               # AI API integration
│
├── repositories/                   # Data access layer
│   ├── __init__.py
│   └── session_repository.py       # Streamlit session state management
│
├── ui/                             # User interface layer
│   ├── __init__.py
│   ├── components/                 # Reusable UI components
│   │   ├── __init__.py
│   │   ├── file_upload.py          # File upload component
│   │   ├── dashboard.py            # Dashboard summary cards
│   │   ├── charts.py               # Enhanced chart components
│   │   ├── tables.py               # Enhanced table components
│   │   └── interpretation.py       # AI interpretation component
│   ├── layouts/                    # Layout components
│   │   ├── __init__.py
│   │   └── main_layout.py          # Main layout and custom CSS
│   └── pages/                      # Page components (for future expansion)
│       └── __init__.py
│
├── utils/                          # Utility functions
│   ├── __init__.py
│   ├── statistics.py               # Statistical helper functions
│   ├── validators.py               # Input validation utilities
│   └── formatters.py               # Data formatting utilities
│
├── modules/                        # Legacy modules (maintained for compatibility)
│   ├── parser.py                   # Original parser (now wraps ParsingService)
│   ├── analyzer.py                 # Original analyzer (now wraps AnalysisService)
│   ├── visualizer.py               # Original visualizer (now wraps VisualizationService)
│   └── ai_interpreter.py           # Original AI interpreter (now wraps AIService)
│
└── tests/                          # Test suite (structure ready)
    ├── __init__.py
    ├── unit/                       # Unit tests
    ├── integration/                # Integration tests
    └── fixtures/                   # Test fixtures
```

## 🏗️ Architecture

The application follows a **layered architecture** pattern for maintainability and scalability:

### Layer Overview

1. **Domain Layer** (`domain/`): Core business models and entities
   - Defines data structures (ParsedFile, MetricValue, AnalysisResult)
   - Custom exceptions for error handling
   - Domain enums for type safety

2. **Service Layer** (`services/`): Business logic and orchestration
   - File operations, parsing, analysis, visualization, AI integration
   - Stateless services that operate on domain models

3. **Repository Layer** (`repositories/`): Data access abstraction
   - Manages Streamlit session state
   - Provides clean interface for data persistence

4. **UI Layer** (`ui/`): User interface components
   - Reusable components (charts, tables, dashboard)
   - Layout management and styling
   - Thin layer that delegates to services

5. **Configuration Layer** (`config/`): Centralized configuration
   - Settings, constants, and UI configuration
   - Environment-specific values

6. **Utilities** (`utils/`): Shared helper functions
   - Statistics, validation, formatting

### Design Principles

- **Separation of Concerns**: Each layer has a specific responsibility
- **Dependency Injection**: Services receive dependencies rather than creating them
- **Type Safety**: Extensive use of type hints throughout
- **Error Handling**: Custom exception hierarchy for better error messages
- **Backward Compatibility**: Legacy modules maintained for compatibility

## 🔧 Configuration

### AI API Configuration

Edit `config/settings.py` to configure your AI provider:

```python
AI_API_BASE_URL = "https://your-api-endpoint.com/v1"
AI_API_MODEL = "your-model-name"
AI_API_ENDPOINT = f"{AI_API_BASE_URL}/models/{AI_API_MODEL}:generateContent"
```

### UI Configuration

Customize UI elements in `config/ui_config.py`:
- App title and subtitle
- Button text
- Color schemes
- Layout settings

### Constants

Application-wide constants in `config/constants.py`:
- Chart colors
- File size limits
- Analysis thresholds

## 🧪 Testing

The project structure includes a `tests/` directory ready for test implementation. To add tests:

1. Create test files in `tests/unit/` or `tests/integration/`
2. Use pytest or your preferred testing framework
3. Add test fixtures in `tests/fixtures/`

## 🔌 Extending the Application

The modular architecture makes it easy to add new features:

### Adding New Chart Types

1. Add chart function to `ui/components/charts.py`
2. Add chart type option in `app.py` chart selector
3. Create display function in `app.py`

### Adding New Analysis Functions

1. Add statistical function to `utils/statistics.py`
2. Integrate into `services/analysis_service.py`
3. Update UI to display results

### Adding New File Formats

1. Extend `services/parsing_service.py` with new parser
2. Update `services/file_service.py` validation
3. Add format detection logic

### Adding New AI Providers

1. Update `config/settings.py` with new provider settings
2. Modify `services/ai_service.py` to support new API format
3. Update prompt building if needed

## 📝 Dependencies

### Core Dependencies
- `streamlit>=1.28.0` - Web application framework
- `plotly>=5.17.0` - Interactive charting library
- `pandas>=2.0.0` - Data manipulation and analysis
- `numpy>=1.24.0` - Numerical computing
- `requests>=2.31.0` - HTTP library for AI API calls

### Optional Dependencies
- `openpyxl>=3.1.0` - Excel file export support

## 🐛 Troubleshooting

### Charts not displaying
- Ensure Plotly is properly installed: `pip install plotly`
- Check browser console for JavaScript errors
- Try clearing browser cache

### Excel export not working
- Install openpyxl: `pip install openpyxl`

### AI interpretation fails
- Verify API key is set in `.streamlit/secrets.toml` or environment variable
- Check API endpoint configuration in `config/settings.py`
- Verify network connectivity

### File upload issues
- Ensure files are plain text (.txt) format
- Check file size limits in `config/constants.py`
- Verify file encoding is UTF-8

## 📄 License

[Add your license information here]

## 🤝 Contributing

[Add contribution guidelines here]

## 📧 Support

[Add support/contact information here]

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Charts powered by [Plotly](https://plotly.com/python/)
- Data analysis with [Pandas](https://pandas.pydata.org/)
