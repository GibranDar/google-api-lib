from typing import TypedDict, Literal

RecalculationInterval = Literal["RECALCULATION_INTERVAL_UNSPECIFIED", "ON_CHANGE", "MINUTE", "HOUR"]
NumberFormatType = Literal[
    "NUMBER_FORMAT_TYPE_UNSPECIFIED",
    "TEXT",
    "NUMBER",
    "PERCENT",
    "CURRENCY",
    "DATE",
    "TIME",
    "DATE_TIME",
    "SCIENTIFIC",
]
ThemeColorType = Literal[
    "THEME_COLOR_TYPE_UNSPECIFIED",
    "TEXT",
    "BACKGROUND",
    "ACCENT1",
    "ACCENT2",
    "ACCENT3",
    "ACCENT4",
    "ACCENT5",
    "ACCENT6",
    "LINK",
]
Style = Literal[
    "STYLE_UNSPECIFIED", "DOTTED", "DASHED", "SOLID", "SOLID_MEDIUM", "SOLID_THICK", "NONE", "DOUBLE"
]
HorizontalAlign = Literal["HORIZONTAL_ALIGN_UNSPECIFIED", "LEFT", "CENTER", "RIGHT"]
VerticalAlign = Literal["VERTICAL_ALIGN_UNSPECIFIED", "TOP", "MIDDLE", "BOTTOM"]
WrapStrategy = Literal["WRAP_STRATEGY_UNSPECIFIED", "OVERFLOW_CELL", "LEGACY_WRAP", "CLIP", "WRAP"]
TextDirection = Literal["TEXT_DIRECTION_UNSPECIFIED", "LEFT_TO_RIGHT", "RIGHT_TO_LEFT"]
HyperlinkDisplayType = Literal["HYPERLINK_DISPLAY_TYPE_UNSPECIFIED", "LINKED", "PLAIN_TEXT"]
SheetType = Literal["SHEET_TYPE_UNSPECIFIED", "GRID", "OBJECT", "DATA_SOURCE"]
ErrorType = Literal[
    "ERROR_TYPE_UNSPECIFIED",
    "ERROR",
    "NULL_VALUE",
    "DIVIDE_BY_ZERO",
    "VALUE",
    "REF",
    "NAME",
    "NUM",
    "N_A",
    "LOADING",
]
ConditionType = Literal[
    "CONDITION_TYPE_UNSPECIFIED",
    "NUMBER_GREATER",
    "NUMBER_GREATER_THAN_EQUAL",
    "NUMBER_LESS",
    "NUMBER_LESS_THAN_EQUAL",
    "NUMBER_EQUAL",
    "NUMBER_NOT_EQUAL",
    "NUMBER_BETWEEN",
    "NUMBER_NOT_BETWEEN",
    "TEXT_CONTAINS",
    "TEXT_NOT_CONTAINS",
    "TEXT_STARTS_WITH",
    "TEXT_ENDS_WITH",
    "TEXT_EQUAL",
    "TEXT_IS_EMAIL",
    "TEXT_IS_URL",
    "DATE_EQUAL",
    "DATE_BEFORE",
    "DATE_AFTER",
    "DATE_ON_OR_BEFORE",
    "DATE_ON_OR_AFTER",
    "DATE_BETWEEN",
    "DATE_NOT_BETWEEN",
    "DATE_IS_VALID",
    "ONE_OF_RANGE",
    "ONE_OF_LIST",
    "BLANK",
    "NOT_BLANK",
    "CUSTOM_FORMULA",
    "BOOLEAN",
    "TEXT_NOT_EQUAL",
    "DATE_NOT_EQUAL",
]
SortOrder = Literal["SORT_ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]
DateTimeRuleType = Literal[
    "DATE_TIME_RULE_TYPE_UNSPECIFIED",
    "SECOND",
    "MINUTE",
    "HOUR",
    "HOUR_MINUTE",
    "HOUR_MINUTE_AMPM",
    "DAY_OF_WEEK",
    "DAY_OF_YEAR",
    "DAY_OF_MONTH",
    "DAY_MONTH",
    "MONTH",
    "QUARTER",
    "YEAR",
    "YEAR_MONTH",
    "YEAR_QUARTER",
    "YEAR_MONTH_DAY",
]
PivotValueSummarizeFunction = Literal[
    "PIVOT_VALUE_SUMMARIZE_FUNCTION_UNSPECIFIED",
    "SUM",
    "COUNTA",
    "COUNT",
    "COUNTUNIQUE",
    "AVERAGE",
    "MAX",
    "MIN",
    "MEDIAN",
    "PRODUCT",
    "STDEV",
    "STDEVP",
    "VAR",
    "VARP",
    "CUSTOM",
]
PivotValueCalculatedDisplayType = Literal[
    "PIVOT_VALUE_CALCULATED_DISPLAY_TYPE_UNSPECIFIED",
    "PERCENT_OF_ROW_TOTAL",
    "PERCENT_OF_COLUMN_TOTAL",
    "PERCENT_OF_GRAND_TOTAL",
]
PivotValueLayout = Literal["HORIZONTAL", "VERTICAL"]
DataSourceTableColumnSelectionType = Literal[
    "DATA_SOURCE_TABLE_COLUMN_SELECTION_TYPE_UNSPECIFIED", "SELECTED", "SYNC_ALL"
]
DeveloperMetadataLocationType = Literal[
    "DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED", "ROW", "COLUMN", "SHEET", "SPREADSHEET"
]
Dimension = Literal["DIMENSION_UNSPECIFIED", "ROWS", "COLUMNS"]
DeveloperMetadataVisibility = Literal["DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED", "DOCUMENT", "PROJECT"]
LineDashType = Literal[
    "LINE_DASH_TYPE_UNSPECIFIED",
    "INVISIBLE",
    "CUSTOM",
    "SOLID",
    "DOTTED",
    "MEDIUM_DASHED",
    "MEDIUM_DASHED_DOTTED",
    "LONG_DASHED",
    "LONG_DASHED_DOTTED",
]


class Color(TypedDict):
    red: float
    green: float
    blue: float
    alpha: float


class ColorStyle(TypedDict, total=False):
    rgbColor: Color
    themeColor: ThemeColorType


class LineStyle(TypedDict):
    width: int


class Padding(TypedDict):
    top: int
    right: int
    bottom: int
    left: int


class Border(TypedDict):
    style: Style
    width: int
    color: Color
    colorStyle: ColorStyle


class Borders(TypedDict):
    top: Border
    bottom: Border
    left: Border
    right: Border


class Link(TypedDict, total=False):
    uri: str


class TextRotation(TypedDict, total=False):
    angle: int
    vertical: bool


class TextFormat(TypedDict):
    foregroundColor: Color
    foregroundColorStyle: ColorStyle
    fontFamily: str
    fontSize: int
    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    link: Link


class NumberFormat(TypedDict):
    type: NumberFormatType
    pattern: str


class CellFormat(TypedDict):
    numberFormat: NumberFormat
    backgroundColor: Color
    backgroundColorStyle: ColorStyle
    borders: Borders
    padding: Padding
    horizontalAlignment: HorizontalAlign
    verticalAlignment: VerticalAlign
    wrapStrategy: WrapStrategy
    textDirection: TextDirection
    textFormat: TextFormat
    hyperlinkDisplayType: HyperlinkDisplayType
    textRotation: TextRotation


class ThemeColorPair(TypedDict):
    colorType: ThemeColorType
    color: ColorStyle


class IterativeCalculationSettings(TypedDict):
    maxIterations: int
    convergenceThreshold: float


class SpreadsheetTheme(TypedDict):
    primaryFontFamily: str
    themeColors: list[ThemeColorPair]


class SpreadsheetProperties(TypedDict):
    title: str
    locale: str
    autoRecalc: RecalculationInterval
    timeZone: str
    defaultFormat: CellFormat
    iterativeCalculationSettings: IterativeCalculationSettings
    spreadsheetTheme: SpreadsheetTheme


class GridProperties(TypedDict):
    rowCount: int
    columnCount: int
    frozenRowCount: int
    frozenColumnCount: int
    hideGridlines: bool
    rowGroupControlAfter: bool
    columnGroupControlAfter: bool


class DataSourceColumnReference(TypedDict):
    name: str


class DataSourceColumn(TypedDict):
    reference: DataSourceColumnReference
    formula: str


DataExecutionState = Literal[
    "DATA_EXECUTION_STATE_UNSPECIFIED", "NOT_STARTED", "RUNNING", "SUCCEEDED", "FAILED"
]


class DataExecutionStatus(TypedDict):
    state: DataExecutionState
    errorCode: str
    errorMessage: str
    lastRefreshTime: str


class DataSourceSheetProperties(TypedDict):
    dataSourceId: str
    columns: list[DataSourceColumn]
    dataExecutionStatus: DataExecutionStatus


class SheetProperties(TypedDict):
    sheetId: int
    title: str
    index: int
    sheetType: SheetType
    gridProperties: GridProperties
    hidden: bool
    tabColor: Color
    tabColorStyle: ColorStyle
    rightToLeft: bool
    dataSourceSheetProperties: DataSourceSheetProperties


class ErrorValue(TypedDict):
    type: ErrorType
    message: str


class ExtendedValue(TypedDict, total=False):
    numberValue: float
    stringValue: str
    boolValue: bool
    formulaValue: str
    errorValue: ErrorValue


class TextFormatRun(TypedDict):
    startIndex: int
    format: TextFormat


RelativeDate = Literal[
    "RELATIVE_DATE_UNSPECIFIED", "PAST_YEAR", "PAST_MONTH", "PAST_WEEK", "YESTERDAY", "TODAY", "TOMORROW"
]


class ConditionValue(TypedDict, total=False):
    relativeDate: RelativeDate
    userEnteredValue: str


class BooleanCondition(TypedDict):
    type: ConditionType
    values: list[ConditionValue]


class DataValidationRule(TypedDict):
    condition: BooleanCondition
    inputMessage: str
    strict: bool
    showCustomUi: bool


class PivotGroupValueMetadata(TypedDict):
    value: ExtendedValue
    collapsed: bool


class PivotGroupSortValueBucket(TypedDict):
    valuesIndex: int
    buckets: list[ExtendedValue]


class ManualRuleGroup(TypedDict):
    groupName: ExtendedValue
    items: list[ExtendedValue]


class ManualRule(TypedDict):
    groups: list[ManualRuleGroup]


class HistogramRule(TypedDict):
    interval: float
    start: float
    end: float


class DateTimeRule(TypedDict):
    type: DateTimeRuleType


class PivotGroupRule(TypedDict, total=False):
    manualRule: ManualRule
    histogramRule: HistogramRule
    dateTimeRule: DateTimeRule


class PivotGroupLimit(TypedDict):
    countLimit: int
    applyOrder: int


class PivotGroupBase(TypedDict):
    showTotals: bool
    valueMetadata: list[PivotGroupValueMetadata]
    sortOrder: SortOrder
    valueBucket: PivotGroupSortValueBucket
    repeatHeadings: bool
    label: str
    groupRule: PivotGroupRule
    groupLimit: PivotGroupLimit


class PivotGroup(PivotGroupBase, total=False):
    sourceColumnOffset: int
    dataSourceColumnReference: DataSourceColumnReference


class PivotFilterCriteria(TypedDict):
    visibleValues: list[str]
    condition: BooleanCondition
    visibleByDefault: bool


class PivotFilterSpecBase(TypedDict):
    filterCriteria: PivotFilterCriteria


class PivotFilterSpec(PivotFilterSpecBase, total=False):
    columnOffsetIndex: int
    dataSourceColumnReference: DataSourceColumnReference


class PivotValueBase(TypedDict):
    summarizeFunction: PivotValueSummarizeFunction
    name: str
    calculatedDisplayType: PivotValueCalculatedDisplayType


class PivotValue(PivotValueBase, total=False):
    sourceColumnOffset: int
    formula: str
    dataSourceColumnReference: DataSourceColumnReference


class PivotTableBase(TypedDict):
    rows: list[PivotGroup]
    columns: list[PivotGroup]
    criteria: dict[int, PivotFilterCriteria]
    filterSpecs: list[PivotFilterSpec]
    values: list[PivotValue]
    valueLayout: PivotValueLayout


class GridRange(TypedDict):
    sheetId: int
    startRowIndex: int
    endRowIndex: int
    startColumnIndex: int
    endColumnIndex: int


class PivotTable(PivotTableBase, total=False):
    source: GridRange
    dataSourceId: str


class FilterCriteria(TypedDict):
    hiddenValues: list[str]
    condition: BooleanCondition
    visibleBackgroundColor: Color
    visibleBackgroundColorStyle: ColorStyle
    visibleForegroundColor: Color
    visibleForegroundColorStyle: ColorStyle


class FilterSpecBase(TypedDict):
    filterCriteria: FilterCriteria


class FilterSpec(FilterSpecBase, total=False):
    columnIdex: int
    dataSourceColumnReference: DataSourceColumnReference


class SortSpecBase(TypedDict):
    sortOrder: SortOrder
    foregroundColor: Color
    foregroundColorStyle: ColorStyle
    backgroundColor: Color
    backgroundColorStyle: ColorStyle


class SortSpec(SortSpecBase, total=False):
    dimensionIndex: int
    dataSourceColumnReference: DataSourceColumnReference


class DataSourceTable(TypedDict):
    dataSourceId: str
    columnSelectionType: DataSourceTableColumnSelectionType
    columns: list[DataSourceColumnReference]
    filterSpecs: list[FilterSpec]
    sortSpecs: list[SortSpec]
    rowLimit: int
    dataExecutionStatus: DataExecutionStatus


class DataSourceFormula(TypedDict):
    dataSourceId: str
    dataExecutionStatus: DataExecutionStatus


class CellData(TypedDict):
    userEnteredValue: ExtendedValue
    effectiveValue: ExtendedValue
    formattedValue: str
    userEnteredFormat: CellFormat
    effectiveFormat: CellFormat
    hyperlink: str
    note: str
    textFormatRuns: list[TextFormatRun]
    dataValidation: DataValidationRule
    pivotTable: PivotTable
    dataSourceTable: DataSourceTable
    dataSourceFormula: DataSourceFormula


class RowData(TypedDict):
    values: list[CellData]


class DimensionRange(TypedDict):
    sheetId: int
    dimension: Dimension
    startIndex: int
    endIndex: int


class DeveloperMetadataLocationBase(TypedDict):
    locationType: DeveloperMetadataLocationType


class DeveloperMetadataLocation(DeveloperMetadataLocationBase, total=False):
    spreadsheet: bool
    sheetId: int
    dimensionRange: DimensionRange


class DeveloperMetadata(TypedDict):
    metadataId: int
    metadataKey: str
    metadataValue: str
    location: DeveloperMetadataLocation
    visibility: DeveloperMetadataVisibility


class DimensionProperties(TypedDict):
    hiddenByFilter: bool
    hiddenByUser: bool
    pixelSize: int
    developerMetadata: list[DeveloperMetadata]
    dataSourceColumnReference: DataSourceColumnReference


class GridData(TypedDict):
    startRow: int
    startColumn: int
    rowData: list[RowData]
    rowMetadata: list[DimensionProperties]
    columnMetadata: list[DimensionProperties]


class ConditionalFormatRuleBase(TypedDict):
    ranges: list[GridRange]


class BooleanRule(TypedDict):
    condition: BooleanCondition
    format: CellFormat


InterpolationPointType = Literal[
    "INTERPOLATION_POINT_TYPE_UNSPECIFIED", "MIN", "MAX", "NUMBER", "PERCENT", "PERCENTILE"
]


class InterpolationPoint(TypedDict):
    color: Color
    colorStyle: ColorStyle
    type: InterpolationPointType
    value: str


class GradientRule(TypedDict):
    minpoint: InterpolationPoint
    midpoint: InterpolationPoint
    maxpoint: InterpolationPoint


class ConditionalFormatRule(ConditionalFormatRuleBase, total=False):
    booleanRule: BooleanRule
    gradientRule: GradientRule


class FilterView(TypedDict):
    filterViewId: int
    title: str
    range: GridRange
    namedRangeId: str
    sortSpecs: list[SortSpec]
    criteria: dict[int, FilterCriteria]
    filterSpecs: list[FilterSpec]


class Editors(TypedDict):
    users: list[str]
    groups: list[str]
    domainUsersCanEdit: bool


class ProtectedRange(TypedDict):
    protectedRangeId: int
    range: GridRange
    namedRangeId: str
    description: str
    warningOnly: bool
    requestingUserCanEdit: bool
    unprotectedRanges: list[GridRange]
    editors: Editors


class BasicFilter(TypedDict):
    range: GridRange
    sortSpecs: list[SortSpec]
    criteria: dict[int, FilterCriteria]
    filterSpecs: list[FilterSpec]


class TextPosition(TypedDict):
    horizontalAlignment: HorizontalAlign


class DataSourceChartProperties(TypedDict):
    dataSourceId: str
    dataExecutionStatus: DataExecutionStatus


ChartHiddenDimensionStrategy = Literal[
    "CHART_HIDDEN_DIMENSION_STRATEGY_UNSPECIFIED",
    "SKIP_HIDDEN_ROWS_AND_COLUMNS",
    "SKIP_HIDDEN_ROWS",
    "SKIP_HIDDEN_COLUMNS",
    "SHOW_ALL",
]


class ChartSpecBase(TypedDict):
    title: str
    altText: str
    titleTextFormat: TextFormat
    titleTextPosition: TextPosition
    subtitle: str
    subtitleTextFormat: TextFormat
    subtitleTextPosition: TextPosition
    fontName: str
    maximized: bool
    backgroundColor: Color
    backgroundColorStyle: ColorStyle
    dataSourceChartProperties: DataSourceChartProperties
    filterSpecs: list[FilterSpec]
    sortSpecs: list[SortSpec]
    hiddenDimensionStrategy: ChartHiddenDimensionStrategy


BasicChartType = Literal[
    "BASIC_CHART_TYPE_UNSPECIFIED", "BAR", "LINE", "AREA", "COLUMN", "SCATTER", "COMBO", "STEPPED_AREA"
]
BasicChartLegendPosition = Literal[
    "BASIC_CHART_LEGEND_POSITION_UNSPECIFIED",
    "BOTTOM_LEGEND",
    "LEFT_LEGEND",
    "RIGHT_LEGEND",
    "TOP_LEGEND",
    "NO_LEGEND",
]
BasicChartAxisPosition = Literal[
    "BASIC_CHART_AXIS_POSITION_UNSPECIFIED", "BOTTOM_AXIS", "LEFT_AXIS", "RIGHT_AXIS"
]
ViewWindowMode = Literal["DEFAULT_VIEW_WINDOW_MODE", "VIEW_WINDOW_MODE_UNSPPORTED", "EXPLICIT", "PRETTY"]


class ChartAxisViewWindowOptions(TypedDict):
    viewWindowMin: float
    viewWindowMax: float
    viewWindowMode: ViewWindowMode


class BasicChartAxis(TypedDict):
    position: BasicChartAxisPosition
    title: str
    format: TextFormat
    titleTextPosition: TextPosition
    viewWindowOptions: ChartAxisViewWindowOptions


class ChartDateTimeRule(TypedDict):
    type: DateTimeRuleType


class ChartHistogramRule(TypedDict):
    minValue: float
    maxValue: float
    intervalSize: float


class ChartGroupRule(TypedDict, total=False):
    dateTimeRule: ChartDateTimeRule
    histogramRule: ChartHistogramRule


ChartAggregateType = Literal[
    "CHART_AGGREGATE_TYPE_UNSPECIFIED", "AVERAGE", "COUNT", "MAX", "MEDIAN", "MIN", "SUM"
]


class ChartSourceRange(TypedDict):
    sources: list[GridRange]


class ChartDataBase(TypedDict):
    groupRule: ChartGroupRule
    aggregateType: ChartAggregateType


class ChartData(TypedDict, total=False):
    sourceRange: ChartSourceRange
    columnReference: DataSourceColumnReference


class BasicChartDomain(TypedDict):
    domain: ChartData
    reversed: bool


DataLabelType = Literal["DATA_LABEL_TYPE_UNSPECIFIED", "NONE", "DATA", "CUSTOM"]
DataLabelPlacement = Literal[
    "DATA_LABEL_PLACEMENT_UNSPECIFIED",
    "CENTER",
    "LEFT",
    "RIGHT",
    "ABOVE",
    "BELOW",
    "INSIDE_END",
    "INSIDE_BASE",
    "OUTSIDE_END",
]


class DataLabel(TypedDict):
    type: DataLabelType
    textFormat: TextFormat
    placement: DataLabelPlacement
    customLabelData: ChartData


PointShape = Literal[
    "POINT_SHAPE_UNSPECIFIED",
    "CIRCLE",
    "DIAMOND",
    "HEXAGON",
    "PENTAGON",
    "SQUARE",
    "STAR",
    "TRIANGLE",
    "X_MARK",
]


class PointStyle(TypedDict):
    size: float
    shape: PointShape


class BasicSeriesDataPointStyleOverride(TypedDict):
    index: int
    color: Color
    colorStyle: ColorStyle
    pointStyle: PointStyle


class BasicChartSeries(TypedDict):
    series: ChartData
    targetAxis: BasicChartAxisPosition
    type: BasicChartType
    lineStyle: LineStyle
    dataLabel: DataLabel
    color: Color
    colorStyle: ColorStyle
    pointStyle: PointStyle
    styleOverrides: list[BasicSeriesDataPointStyleOverride]


BasicChartStackedType = Literal[
    "BASIC_CHART_STACKED_TYPE_UNSPECIFIED", "NOT_STACKED", "STACKED", "PERCENT_STACKED"
]
BasicChartCompareMode = Literal["BASIC_CHART_COMPARE_MODE_UNSPECIFIED", "DATUM", "CATEGORY"]


class BasicChartSpec(TypedDict):
    chartType: BasicChartType
    legendPosition: BasicChartLegendPosition
    axis: list[BasicChartAxis]
    domains: list[BasicChartDomain]
    series: list[BasicChartSeries]
    headerCount: int
    threeDimensional: bool
    interpolateNulls: bool
    stackedType: BasicChartStackedType
    lineSmoothing: bool
    compareMode: BasicChartCompareMode
    totalDataLabel: DataLabel


PieChartLegendPosition = Literal[
    "PIE_CHART_LEGEND_POSITION_UNSPECIFIED",
    "BOTTOM_LEGEND",
    "LEFT_LEGEND",
    "RIGHT_LEGEND",
    "TOP_LEGEND",
    "NO_LEGEND",
    "LABELLED_LEGEND",
]


class PieChartSpec(TypedDict):
    legendPosition: PieChartLegendPosition
    domain: ChartData
    series: ChartData
    threeDimensional: bool
    pieHole: float


BubbleChartLegendPosition = Literal[
    "BUBBLE_CHART_LEGEND_POSITION_UNSPECIFIED",
    "BOTTOM_LEGEND",
    "LEFT_LEGEND",
    "RIGHT_LEGEND",
    "TOP_LEGEND",
    "NO_LEGEND",
    "INSIDE_LEGEND",
]


class BubbleChartSpec(TypedDict):
    legendPosition: BubbleChartLegendPosition
    bubbleLabels: ChartData
    domain: ChartData
    series: ChartData
    groupIds: ChartData
    bubbleSizes: ChartData
    bubbleOpacity: float
    bubbleBorderColor: Color
    bubbleBorderColorStyle: ColorStyle
    bubbleMaxRadiusSize: int
    bubbleMinRadiusSize: int
    bubbleTextStyle: TextFormat


class CandlestickDomain(TypedDict):
    data: ChartData
    reversed: bool


class CandlestickSeries(TypedDict):
    data: ChartData


class CandlestickData(TypedDict):
    lowSeries: CandlestickSeries
    openSeries: CandlestickSeries
    closeSeries: CandlestickSeries
    highSeries: CandlestickSeries


class CandlestickChartSpec(TypedDict):
    domain: CandlestickDomain
    data: list[CandlestickData]


OrgChartNodeSize = Literal["ORG_CHART_LABEL_SIZE_UNSPECIFIED", "SMALL", "MEDIUM", "LARGE"]


class OrgChartSpec(TypedDict):
    nodeSize: OrgChartNodeSize
    nodeColor: Color
    nodeColorStyle: ColorStyle
    selectedNodeColor: Color
    selectedNodeColorStyle: ColorStyle
    labels: ChartData
    parentLabels: ChartData
    tooltips: ChartData


class HistogramSeries(TypedDict):
    barColor: Color
    barColorStyle: ColorStyle
    data: ChartData


HistogramChartLegendPosition = Literal[
    "HISTOGRAM_CHART_LEGEND_POSITION_UNSPECIFIED",
    "BOTTOM_LEGEND",
    "LEFT_LEGEND",
    "RIGHT_LEGEND",
    "TOP_LEGEND",
    "NO_LEGEND",
    "INSIDE_LEGEND",
]


class HistogramChartSpec(TypedDict):
    series: list[HistogramSeries]
    legendPosition: HistogramChartLegendPosition
    showItemDividers: bool
    bucketSize: float
    outlierPercentile: float


class WaterfallChartDomain(TypedDict):
    data: ChartData
    reversed: bool


class WaterfallChartColumnStyle(TypedDict):
    label: str
    color: Color
    colorStyle: ColorStyle


class WaterfallChartCustomSubtotal(TypedDict):
    subtotalIndex: int
    label: str
    dataIsSubtotal: bool


class WaterfallChartSeries(TypedDict):
    data: ChartData
    negativeColumnsStyle: WaterfallChartColumnStyle
    positiveColumnsStyle: WaterfallChartColumnStyle
    subtotalColumnsStyle: WaterfallChartColumnStyle
    connectorLineStyle: LineStyle
    hideTrailingSubtotal: bool
    customSubtotals: list[WaterfallChartCustomSubtotal]
    dataLabel: DataLabel


WaterfallChartStackedType = Literal["WATERFALL_STACKED_TYPE_UNSPECIFIED", "STACKED", "SEQUENTIAL"]


class WaterfallChartSpec(TypedDict):
    domain: WaterfallChartDomain
    series: list[WaterfallChartSeries]
    stackedType: WaterfallChartStackedType
    firstValueIsTotal: bool
    hideConnectorLines: bool
    connectorLineStyle: LineStyle
    totalDataLabel: DataLabel


class TreemapChartColorScale(TypedDict):
    minValueColor: Color
    minValueColorStyle: ColorStyle
    midValueColor: Color
    midValueColorStyle: ColorStyle
    maxValueColor: Color
    maxValueColorStyle: ColorStyle
    noDataColor: Color
    noDataColorStyle: ColorStyle


class TreemapChartSpec(TypedDict):
    labels: ChartData
    parentLabels: ChartData
    sizeData: ChartData
    colorData: ChartData
    textFormat: TextFormat
    levels: int
    hintedLevels: int
    minValue: float
    maxValue: float
    headerColor: Color
    headerColorStyle: ColorStyle
    colorScale: TreemapChartColorScale
    hideTooltips: bool


class KeyValueFormat(TypedDict):
    textFormat: TextFormat
    position: TextPosition


ComparisonType = Literal["COMPARISON_TYPE_UNDEFINED", "ABSOLUTE_DIFFERENCE", "PERCENTAGE_DIFFERENCE"]


class BaselineValueFormat(TypedDict):
    comparisonType: ComparisonType
    textFormat: TextFormat
    position: TextPosition
    description: str
    positiveColor: Color
    positiveColorStyle: ColorStyle
    negativeColor: Color
    negativeColorStyle: ColorStyle


ChartNumberFormatSource = Literal["CHART_NUMBER_FORMAT_SOURCE_UNDEFINED", "FROM_DATA", "CUSTOM"]


class ChartCustomNumberFormatOptions(TypedDict):
    prefix: str
    suffix: str


class ScorecardChartSpec(TypedDict):
    keyValueData: ChartData
    baselineValueData: ChartData
    aggregateType: ChartAggregateType
    keyValueFormat: KeyValueFormat
    baselineValueFormat: BaselineValueFormat
    scaleFactor: float
    numberFormatSource: ChartNumberFormatSource
    customFormatOptions: ChartCustomNumberFormatOptions


class ChartSpec(ChartSpecBase, total=False):
    basicChart: BasicChartSpec
    pieChart: PieChartSpec
    bubbleChart: BubbleChartSpec
    candlestickChart: CandlestickChartSpec
    orgChart: OrgChartSpec
    histogramChart: HistogramChartSpec
    waterfallChart: WaterfallChartSpec
    treemapChart: TreemapChartSpec
    scorecardChart: ScorecardChartSpec


class GridCoordinate(TypedDict):
    sheetId: int
    rowIndex: int
    columnIndex: int


class OverlayPosition(TypedDict):
    anchorCell: GridCoordinate
    offsetXPixels: int
    offsetYPixels: int
    widthPixels: int
    heightPixels: int


class EmbeddedObjectPosition(TypedDict, total=False):
    sheetId: int
    overlayPosition: OverlayPosition
    newSheet: bool


class EmbeddedObjectBorder(TypedDict):
    color: Color
    colorStyle: ColorStyle


class EmbeddedChart(TypedDict):
    chartId: int
    spec: ChartSpec
    position: EmbeddedObjectPosition
    border: EmbeddedObjectBorder


class BandingProperties(TypedDict):
    headerColor: Color
    headerColorStyle: ColorStyle
    firstBandColor: Color
    firstBandColorStyle: ColorStyle
    secondBandColor: Color
    secondBandColorStyle: ColorStyle
    footerColor: Color
    footerColorStyle: ColorStyle


class BandedRange(TypedDict):
    bandedRangeId: int
    range: GridRange
    rowProperties: BandingProperties
    columnProperties: BandingProperties


class DimensionGroup(TypedDict):
    range: DimensionRange
    depth: int
    collapsed: bool


class SlicerSpec(TypedDict):
    dataRange: GridRange
    filterCriteria: FilterCriteria
    columnIndex: int
    applyToPivotTables: bool
    title: str
    textFormat: TextFormat
    backgroundColor: Color
    backgroundColorStyle: ColorStyle
    horizontalAlignment: HorizontalAlign


class Slicer(TypedDict):
    slicerId: int
    spec: SlicerSpec
    position: EmbeddedObjectPosition


class Sheet(TypedDict):
    properties: SheetProperties
    data: list[GridData]
    merges: list[GridRange]
    conditionalFormats: list[ConditionalFormatRule]
    filterViews: list[FilterView]
    protectedRanges: list[ProtectedRange]
    basicFilter: BasicFilter
    charts: list[EmbeddedChart]
    bandedRanges: list[BandedRange]
    developerMetadata: list[DeveloperMetadata]
    rowGroups: list[DimensionGroup]
    columnGroups: list[DimensionGroup]
    slicers: list[Slicer]


class NamedRange(TypedDict):
    namedRangeId: str
    name: str
    range: GridRange


class DataSourceParameterName(TypedDict, total=False):
    name: str


class DataSourceParameterRange(TypedDict, total=False):
    namedRangeId: str
    range: GridRange


class DataSourceParameter(DataSourceParameterName, DataSourceParameterRange, total=False):
    pass


class BigQueryQuerySpec(TypedDict):
    rawQuery: str


class BigQueryTableSpec(TypedDict):
    tableProjectId: str
    tableId: str
    datasetId: str


class BigQueryDataSourceSpecBase(TypedDict):
    projectId: str


class BigQueryDataSourceSpec(TypedDict, total=False):
    querySpec: BigQueryQuerySpec
    tableSpec: BigQueryTableSpec


class DataSourceSpecBase(TypedDict):
    parameters: list[DataSourceParameter]


class DataSourceSpec(TypedDict, total=False):
    bigQuery: BigQueryDataSourceSpec


class DataSource(TypedDict):
    dataSourceId: str
    spec: DataSourceSpec
    calculatedColumns: list[DataSourceColumn]
    sheetId: int


DataRefreshScope = Literal["DATA_REFRESH_SCOPE_UNSPECIFIED", "ALL_DATA_SOURCES"]


class Interval(TypedDict):
    startTime: str
    endTime: str


class DataSourceRefreshScheduleBase(TypedDict):
    enabled: bool
    refreshScope: DataRefreshScope
    nextRun: Interval


class TimeOfDay(TypedDict):
    hours: int
    minutes: int
    seconds: int
    nanos: int


class DataSourceRefreshDailySchedule(TypedDict):
    startTime: TimeOfDay


class DataSourceRefreshWeeklySchedule(TypedDict):
    startTime: TimeOfDay
    daysOfWeek: Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "SUNDAY",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
    ]


class DataSourceRefreshMonthlySchedule(TypedDict):
    startTime: TimeOfDay
    daysOfMonth: list[int]


class DataSourceRefreshSchedule(TypedDict, total=False):
    dailySchedule: DataSourceRefreshDailySchedule
    weeklySchedule: DataSourceRefreshWeeklySchedule
    monthlySchedule: DataSourceRefreshMonthlySchedule


class Spreadsheet(TypedDict):
    spreadsheetId: str
    properties: SpreadsheetProperties
    sheets: list[Sheet]
    namedRanges: list[NamedRange]
    spreadsheetUrl: str
    developerMetadata: list[DeveloperMetadata]
    dataSources: list[DataSource]
    dataSourceSchedules: list[DataSourceRefreshSchedule]
