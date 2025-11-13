# VNG Data Analyzer - Architecture Documentation

## Overview

The VNG Data Analyzer follows a **layered architecture** pattern with clear separation of concerns, making the codebase maintainable, testable, and extensible.

## Architecture Layers

### 1. Domain Layer (`domain/`)

**Purpose**: Core business logic and domain models

**Contents**:
- `models.py`: Domain entities (ParsedFile, MetricValue, MetricData, AnalysisResult, AnalysisResults)
- `enums.py`: Domain enumerations (ChartType, AnalysisStatus, MetricChangeType)
- `exceptions.py`: Domain-specific exceptions (VNGError, ParsingError, AnalysisError, etc.)

**Principles**:
- Pure Python classes with no external dependencies
- Represents the core business concepts
- No knowledge of UI or infrastructure

### 2. Service Layer (`services/`)

**Purpose**: Business logic orchestration

**Services**:
- `file_service.py`: File validation and reading operations
- `parsing_service.py`: VNG file parsing logic
- `analysis_service.py`: Statistical analysis operations
- `visualization_service.py`: Chart generation
- `ai_service.py`: AI interpretation integration

**Principles**:
- Contains business logic
- Uses domain models
- Can call other services
- No direct UI dependencies

### 3. Repository Layer (`repositories/`)

**Purpose**: Data access abstraction

**Repositories**:
- `session_repository.py`: Streamlit session state management

**Principles**:
- Abstracts data access
- Provides clean interface for data operations
- Isolates infrastructure concerns

### 4. Configuration Layer (`config/`)

**Purpose**: Application configuration management

**Modules**:
- `settings.py`: Application settings (API keys, endpoints, etc.)
- `constants.py`: Application constants (colors, file limits, etc.)
- `ui_config.py`: UI-specific configuration and text constants

**Principles**:
- Centralized configuration
- Environment-aware (supports env vars)
- Type-safe settings

### 5. UI Layer (`ui/`)

**Purpose**: Presentation and user interface

**Structure**:
- `components/`: Reusable UI components (to be implemented)
- `pages/`: Page-level components (to be implemented)
- `layouts/`: Layout structures (to be implemented)

**Principles**:
- Thin presentation layer
- Delegates business logic to services
- Uses repositories for data access

### 6. Utilities (`utils/`)

**Purpose**: Shared utility functions

**Modules**:
- `statistics.py`: Statistical calculations
- `validators.py`: Input validation utilities
- `formatters.py`: Data formatting utilities

**Principles**:
- Pure functions where possible
- No side effects
- Reusable across layers

### 7. Legacy Modules (`modules/`)

**Purpose**: Backward compatibility and low-level operations

**Modules**:
- `parser.py`: Low-level parsing functions
- `analyzer.py`: Low-level analysis functions
- `visualizer.py`: Low-level chart rendering
- `ai_interpreter.py`: Low-level AI API calls

**Note**: These are wrapped by services but kept for backward compatibility and direct access when needed.

## Data Flow

```
User Input (UI)
    ↓
app.py (Entry Point)
    ↓
Services (Business Logic)
    ↓
Domain Models (Data Structures)
    ↓
Legacy Modules (Low-level Operations)
    ↓
Results → Repository → UI
```

## Key Design Patterns

### 1. Service Layer Pattern
- Business logic encapsulated in service classes
- Services are stateless and reusable
- Clear interfaces for operations

### 2. Repository Pattern
- Abstracts data access
- Centralized session state management
- Easy to mock for testing

### 3. Domain Model Pattern
- Rich domain models with behavior
- Type-safe data structures
- Clear business concepts

### 4. Dependency Injection
- Services can be easily swapped
- Testable components
- Loose coupling

## Benefits

1. **Maintainability**: Clear separation of concerns makes code easy to understand and modify
2. **Testability**: Each layer can be tested independently
3. **Extensibility**: New features can be added without affecting existing code
4. **Type Safety**: Comprehensive type hints throughout
5. **Error Handling**: Centralized exception hierarchy
6. **Configuration**: Environment-aware settings management

## Migration Path

The architecture maintains backward compatibility:
- Old `config.py` still works (imports from new structure)
- Legacy modules still accessible
- Gradual migration possible

## Future Enhancements

- Add dependency injection container
- Implement comprehensive unit tests
- Add integration tests
- Create UI component library
- Add logging infrastructure
- Implement caching layer

