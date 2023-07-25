from typing import TypedDict, Literal, Union, Any

Unit = Literal["UNIT_UNSPECIFIED", "EMU", "PT"]
Alignment = Literal["ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END", "JUSTIFIED"]
TextDirection = Literal["TEXT_DIRECTION_UNSPECIFIED", "LEFT_TO_RIGHT", "RIGHT_TO_LEFT"]
SpacingMode = Literal["SPACING_MODE_UNSPECIFIED", "NEVER_COLLAPSE", "COLLAPSE_LISTS"]
BaselineOffset = Literal["BASELINE_OFFSET_UNSPECIFIED", "NONE", "SUPERSCRIPT", "SUBSCRIPT"]
AutoTextType = Literal["TYPE_UNSPECIFIED", "SLIDE_NUMBER"]
RelativeSlideLink = Literal[
    "RELATIVE_SLIDE_LINK_UNSPECIFIED", "PREVIOUS_SLIDE", "NEXT_SLIDE", "FIRST_SLIDE", "LAST_SLIDE"
]
PropertyState = Literal["INHERIT", "RENDERED", "NOT_RENDERED"]
DashStyle = Literal[
    "DASH_STYLE_UNSPECIFIED", "SOLID", "DOT", "DASH", "DASH_DOT", "LONG_DASH", "LONG_DASH_DOT"
]
RectanglePosition = Literal[
    "RECTANGLE_POSITION_UNSPECIFIED",
    "TOP_LEFT",
    "TOP_CENTER",
    "TOP_RIGHT",
    "LEFT_CENTER",
    "CENTER",
    "RIGHT_CENTER",
    "BOTTOM_LEFT",
    "BOTTOM_CENTER",
    "BOTTOM_RIGHT",
]
ContentAlignment = Literal[
    "CONTENT_ALIGNMENT_UNSPECIFIED", "CONTENT_ALIGNMENT_UNSUPPORTED", "TOP", "MIDDLE", "BOTTOM"
]


class AffineTransform(TypedDict):
    scaleX: float
    scaleY: float
    shearX: float
    shearY: float
    translateX: float
    translateY: float
    unit: Unit


class Dimension(TypedDict):
    magnitude: float
    unit: Unit


class WeightedFontFamily(TypedDict):
    fontFamily: str
    weight: int


class RgbColor(TypedDict):
    red: float
    green: float
    blue: float


class OpaqueColor(TypedDict, total=False):
    rgbColor: RgbColor
    themeColor: str


class OptionalColor(TypedDict):
    opaqueColor: OpaqueColor


class ThemeColorPair(TypedDict):
    type: str
    color: RgbColor


class ColorStop(TypedDict):
    color: OptionalColor
    alpha: float
    position: float


class ColorScheme(TypedDict):
    colors: list[ThemeColorPair]


class Recolor(TypedDict):
    recolorStops: list[ColorStop]
    name: str


class SolidFill(TypedDict):
    color: OpaqueColor
    alpha: int


class Link(TypedDict, total=False):
    url: str
    relativeLink: RelativeSlideLink
    pageObjectId: str
    slideIndex: int


class Size(TypedDict):
    width: Dimension
    height: Dimension


class TextStyle(TypedDict):
    backgroundColor: OptionalColor
    foregroundColor: OptionalColor
    bold: bool
    italic: bool
    fontFamily: str
    fontSize: Dimension
    link: Link
    baselineOffset: BaselineOffset
    smallCaps: bool
    strikethrough: bool
    underline: bool
    weightedFontFamily: WeightedFontFamily


class ParagraphStyle(TypedDict):
    lineSpacing: float
    alignment: Alignment
    indentStart: Dimension
    spaceAbove: Dimension
    spaceBelow: Dimension
    indentFirstLine: Dimension
    direction: TextDirection
    spacingMode: SpacingMode


class Bullet(TypedDict):
    listId: str
    nestingLevel: int
    glyph: str
    bulletStyle: TextStyle


class ParagraphMarker(TypedDict):
    style: ParagraphStyle
    bullet: Bullet


class TextRun(TypedDict):
    content: str
    style: TextStyle


class AutoText(TypedDict):
    type: AutoTextType
    content: str
    style: TextStyle


class TextElementBase(TypedDict):
    startIndex: int
    endIndex: int


class TextElement(TextElementBase, total=False):
    paragraphMarker: ParagraphMarker
    textRun: TextRun
    autoText: AutoText


class NestingLevel(TypedDict):
    bulletStyle: TextStyle


class List(TypedDict):
    listId: str
    nestingLevel: dict[int, NestingLevel]


class TextContent(TypedDict):
    textElements: list[TextElement]
    lists: dict[str, List]


class StretchedPictureFill(TypedDict):
    contentUrl: str
    size: Size


class ShapeBackgroundFillBase(TypedDict):
    propertyState: PropertyState


class ShapeBackgroundFill(ShapeBackgroundFillBase, total=False):
    solidFill: SolidFill


class PageBackgroundFillBase(TypedDict):
    propertyState: PropertyState


class PageBackgroundFill(PageBackgroundFillBase, total=False):
    solidFill: SolidFill
    stretchedPictureFill: StretchedPictureFill


class OutlineFill(TypedDict, total=False):
    solidFill: SolidFill


class LineFill(TypedDict, total=False):
    solidFill: SolidFill


class TableBorderFill(TypedDict, total=False):
    solidFill: SolidFill


class LineConnection(TypedDict):
    connectedObjectId: str
    connectionSiteIndex: int


class Outline(TypedDict):
    outlineFill: OutlineFill
    weight: Dimension
    dashStyle: DashStyle
    propertyState: PropertyState


class Shadow(TypedDict):
    type: Literal["SHADOW_TYPE_UNSPECIFIED", "OUTER"]
    transform: AffineTransform
    alignment: RectanglePosition
    blurRadius: Dimension
    color: OpaqueColor
    alpha: float
    rotateWithShape: bool
    propertyState: PropertyState


class Autofit(TypedDict):
    autofitType: Literal["AUTOFIT_TYPE_UNSPECIFIED", "NONE", "TEXT_AUTOFIT", "SHAPE_AUTOFIT"]
    fontScale: float
    lineSpacingReduction: float


class ShapeProperties(TypedDict):
    shapeBackgroundFill: dict[str, Any]
    outline: Outline
    shadow: Shadow
    link: Link
    contentAlignment: ContentAlignment
    autoFit: Autofit


class CropProperties(TypedDict):
    leftOffset: float
    rightOffset: float
    topOffset: float
    bottomOffset: float
    angle: float


class ImageProperties(TypedDict):
    cropProperties: CropProperties
    transparency: float
    brightness: float
    contrast: float
    recolor: dict[str, Recolor]
    outline: Outline
    shadow: Shadow
    link: Link


class VideoProperties(TypedDict):
    outline: Outline
    autoplay: bool
    start: int
    end: int
    mute: bool


class LineProperties(TypedDict):
    lineFill: LineFill
    weight: Dimension
    dashStyle: DashStyle
    startArrow: str  # https://developers.google.com/slides/api/reference/rest/v1/presentations.pages/lines#Page.ArrowStyle
    endArrow: str  # https://developers.google.com/slides/api/reference/rest/v1/presentations.pages/lines#Page.ArrowStyle
    link: Link
    startConnection: LineConnection
    endConnection: LineConnection


class Placeholder(TypedDict):
    type: Literal[
        "NONE",
        "BODY",
        "CENTERED_TITLE",
        "CHART",
        "CLIP_ART",
        "CENTERED_TITLE",
        "DATE_AND_TIME",
        "FOOTER",
        "HEADER",
        "MEDIA",
        "OBJECT",
        "PICTURE",
        "SLIDE_NUMBER",
        "SUBTITLE",
        "TABLE",
        "TITLE",
        "VERTICAL_OBJECT",
    ]
    index: int
    parentObjectId: str


class Shape(TypedDict):
    shapeType: str
    text: TextContent
    shapeProperties: ShapeProperties
    placeholder: Placeholder


class Image(TypedDict):
    contentUrl: str
    imageProperties: ImageProperties
    sourceUrl: str
    placeholder: Placeholder


class Video(TypedDict):
    url: str
    source: Literal["SOURCE_UNSPECIFIED", "YOUTUBE", "DRIVE"]
    id: str
    videoProperties: VideoProperties


class Line(TypedDict):
    lineProperties: LineProperties
    lineType: str
    lineCategory: Literal["LINE_CATEGORY_UNSPECIFIED", "STRAIGHT", "BENT", "CURVED"]


class TableCellBackgroundFillBase(TypedDict):
    propertyState: PropertyState


class TableCellBackgroundFill(TableCellBackgroundFillBase, total=False):
    solidFill: SolidFill


class TableCellProperties(TypedDict):
    tableCellBackgroundFill: TableCellBackgroundFill
    contentAlignment: ContentAlignment


class TableCellLocation(TypedDict):
    rowIndex: int
    columnIndex: int


class TableRowProperties(TypedDict):
    minRowHeight: Dimension


class TableColumnProperties(TypedDict):
    columnWidth: Dimension


class TableBorderProperties(TypedDict):
    tableBorderFill: TableBorderFill
    weight: Dimension
    dashStyle: DashStyle


class TableBorderCell(TypedDict):
    location: TableCellLocation
    tableBorderProperties: TableBorderProperties


class TableBorderRow(TypedDict):
    tableBorderCells: list[TableBorderCell]


class TableCell(TypedDict):
    location: TableCellLocation
    rowSpan: int
    columnSpan: int
    text: TextContent
    tableCellProperties: TableCellProperties


class TableRow(TypedDict):
    rowHeight: Dimension
    tableRowProperties: TableRowProperties
    tableCells: list[TableCell]


class Table(TypedDict):
    rows: int
    columns: int
    tableRows: list[TableRow]
    tableColumns: list[TableColumnProperties]
    horizontalBorderRows: list[TableBorderRow]
    verticalBorderRows: list[TableBorderRow]


class WordArt(TypedDict):
    renderedText: str


class SheetsChartProperties(TypedDict, total=False):
    chartImageProperties: ImageProperties


class SheetsChart(TypedDict):
    spreadsheetId: str
    chartId: int
    contentUrl: str
    sheetsChartProperties: SheetsChartProperties


class PageElementBase(TypedDict):
    objectId: str
    size: Size
    transform: AffineTransform
    title: str
    description: str


class PageElement(PageElementBase, total=False):
    elementGroup: dict[str, Any]  # { "children": list[PageElement] }
    shape: Shape
    image: Image
    video: Video
    line: Line
    table: Table
    wordArt: WordArt
    sheetsChart: SheetsChart


class PageProperties(TypedDict):
    pageBackgroundFill: dict[str, PageBackgroundFill]
    colorScheme: dict[str, ColorScheme]


class PageBase(TypedDict):
    objectId: str
    pageType: Literal["SLIDE", "MASTER", "LAYOUT", "NOTES", "NOTES_MASTER"]
    pageElements: list[PageElement]
    revisionId: str
    pageProperties: PageProperties


class NotesProperties(TypedDict):
    speakerNotesObjectId: str


class MasterProperties(TypedDict):
    displayName: str


class LayoutProperties(TypedDict):
    masterObjectId: str
    name: str
    displayName: str


class SlideProperties(TypedDict):
    layoutObjectId: str
    masterObjectId: str
    notesPage: PageBase
    isSkipped: bool


class Page(PageBase, total=False):
    slideProperties: SlideProperties
    layoutProperties: LayoutProperties
    notesProperties: NotesProperties
    masterProperties: MasterProperties


class Presentation(TypedDict):
    presentationId: str
    pageSize: Size
    slides: list[Page]
    title: str
    masters: list[Page]
    layouts: list[Page]
    locale: str
    revisionId: str
    notesMaster: Page
