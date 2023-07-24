from typing import TypedDict, Literal, Union

Unit = Literal["UNIT_UNSPECIFIED", "PT"]
BaselineOffset = Literal["BASELINE_OFFSET_UNSPECIFIED", "NONE", "SUPERSCRIPT", "SUBSCRIPT"]
Type = Literal["TYPE_UNSPECIFIED", "PAGE_NUMBER", "PAGE_COUNT"]
NamedStyleType = Literal[
    "NAMED_STYLE_TYPE_UNSPECIFIED",
    "NORMAL_TEXT",
    "TITLE",
    "SUBTITLE",
    "HEADING_1",
    "HEADING_2",
    "HEADING_3",
    "HEADING_4",
    "HEADING_5",
    "HEADING_6",
]
Alignment = Literal["ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END", "JUSTIFIED"]
ContentAlignment = Literal[
    "CONTENT_ALIGNMENT_UNSPECIFIED", "CONTENT_ALIGNMENT_UNSUPPORTED", "TOP", "MIDDLE", "BOTTOM"
]
ContentDirection = Literal["CONTENT_DIRECTION_UNSPECIFIED", "LEFT_TO_RIGHT", "RIGHT_TO_LEFT"]
SpacingMode = Literal["SPACING_MODE_UNSPECIFIED", "NEVER_COLLAPSE", "COLLAPSE_LISTS"]
DashStyle = Literal["DASH_STYLE_UNSPECIFIED", "SOLID", "DOT", "DASH"]
TabStopAlignment = Literal["TAB_STOP_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"]
WidthType = Literal["WIDTH_TYPE_UNSPECIFIED", "EVENLY_DISTRIBUTED", "FIXED_WIDTH"]


class RgbColor(TypedDict):
    red: float
    green: float
    blue: float


class Color(TypedDict):
    rgbColor: dict[str, float]


class OptionalColor(TypedDict):
    color: Color


class Dimension(TypedDict):
    magnitude: float
    unit: Unit


class WeightedFontFamily(TypedDict):
    fontFamily: str
    weight: int


class Link(TypedDict, total=False):
    url: str
    bookmarkId: str
    headingId: str


class TextStyle(TypedDict):
    bold: bool
    italic: bool
    underline: bool
    strikethrough: bool
    smallCaps: bool
    backgroundColor: OptionalColor
    foregroundColor: OptionalColor
    fontSize: Dimension
    weightedFontFamily: WeightedFontFamily
    baselineOffset: BaselineOffset
    link: Link


class TextStyleSuggestionState(TypedDict):
    boldSuggested: bool
    italicSuggested: bool
    underlineSuggested: bool
    strikethroughSuggested: bool
    smallCapsSuggested: bool
    backgroundColorSuggested: bool
    foregroundColorSuggested: bool
    fontSizeSuggested: bool
    weightedFontFamilySuggested: bool
    baselineOffsetSuggested: bool
    linkSuggested: bool


class SuggestedTextStyle(TypedDict):
    textStyle: TextStyle
    textStyleSuggestionState: TextStyleSuggestionState


class TextRun(TypedDict):
    content: str
    suggestedInsertionIds: list[str]
    suggestedDeletionIds: list[str]
    textStyle: TextStyle
    suggestedTextStyleChanges: dict[str, SuggestedTextStyle]


class AutoText(TypedDict):
    type: Type
    suggestedInsertionIds: list[str]
    suggestedDeletionIds: list[str]
    textStyle: TextStyle
    suggestedTextStyleChanges: dict[str, SuggestedTextStyle]


class PageBreak(TypedDict):
    suggestedInsertionIds: list[str]
    suggestedDeletionIds: list[str]
    textStyle: TextStyle
    suggestedTextStyleChanges: dict[str, SuggestedTextStyle]


class ColumnBreak(TypedDict):
    suggestedInsertionIds: list[str]
    suggestedDeletionIds: list[str]
    textStyle: TextStyle
    suggestedTextStyleChanges: dict[str, SuggestedTextStyle]


class FootnoteReference(TypedDict):
    footnoteId: str
    footnoteNumber: str
    suggestedInsertionIds: list[str]
    suggestedDeletionIds: list[str]
    textStyle: TextStyle
    suggestedTextStyleChanges: dict[str, SuggestedTextStyle]


class HorizontalRule(TypedDict):
    suggestedInsertionIds: list[str]
    suggestedDeletionIds: list[str]
    textStyle: TextStyle
    suggestedTextStyleChanges: dict[str, SuggestedTextStyle]


class Equation(TypedDict):
    suggestedInsertionIds: list[str]
    suggestedDeletionIds: list[str]


class InlineObjectElement(TypedDict):
    inlineObjectId: str
    suggestedInsertionIds: list[str]
    suggestedDeletionIds: list[str]
    textStyle: TextStyle
    suggestedTextStyleChanges: dict[str, SuggestedTextStyle]


class PersonProperties(TypedDict):
    name: str
    email: str


class Person(TypedDict):
    personId: str
    suggestedInsertionIds: list[str]
    suggestedDeletionIds: list[str]
    textStyle: TextStyle
    suggestedTextStyleChanges: dict[str, SuggestedTextStyle]
    personProperties: PersonProperties


class RichLinkProperties(TypedDict):
    title: str
    uri: str
    mimeType: str


class RichLink(TypedDict):
    rickLinkId: str
    suggestedInsertionIds: list[str]
    suggestedDeletionIds: list[str]
    textStyle: TextStyle
    suggestedTextStyleChanges: dict[str, SuggestedTextStyle]
    richLinkProperties: RichLinkProperties


class ParagraphElementBase(TypedDict):
    startIndex: int
    endIndex: int


class ParagraphElement(ParagraphElementBase, total=False):
    textRun: TextRun
    autoText: AutoText
    pageBreak: PageBreak
    columnBreak: ColumnBreak
    footnoteReference: FootnoteReference
    horizontalRule: HorizontalRule
    equation: Equation
    inlineObjectElement: InlineObjectElement
    person: Person
    richLink: RichLink


class ParagraphBorder(TypedDict):
    color: Color
    width: Dimension
    dashStyle: DashStyle


class TabStop(TypedDict):
    offset: Dimension
    alignment: TabStopAlignment


class Shading(TypedDict):
    backgroundColor: OptionalColor


class ParagraphStyle(TypedDict):
    headingId: str
    namedStyleType: NamedStyleType
    alignment: Alignment
    lineSpacing: float
    direction: ContentDirection
    spacingMode: SpacingMode
    spaceAbove: Dimension
    spaceBelow: Dimension
    borderBetween: ParagraphBorder
    borderTop: ParagraphBorder
    borderBottom: ParagraphBorder
    borderLeft: ParagraphBorder
    borderRight: ParagraphBorder
    indentFirstLine: Dimension
    indentStart: Dimension
    indentEnd: Dimension
    tabStops: list[TabStop]
    keepLinesTogether: bool
    keepWithNext: bool
    shading: Shading
    pageBreakBefore: bool


class ShadingSuggestionState(TypedDict):
    backgroundColorSuggested: bool


class ParagraphStyleSuggestionState(TypedDict):
    headingIdSuggested: bool
    namedStyleTypeSuggested: bool
    alignmentSuggested: bool
    lineSpacingSuggested: bool
    directionSuggested: bool
    spacingModeSuggested: bool
    spaceAboveSuggested: bool
    spaceBelowSuggested: bool
    borderBetweenSuggested: bool
    borderTopSuggested: bool
    borderBottomSuggested: bool
    borderLeftSuggested: bool
    borderRightSuggested: bool
    indentFirstLineSuggested: bool
    indentStartSuggested: bool
    indentEndSuggested: bool
    keepLinesTogetherSuggested: bool
    keepWithNextSuggested: bool
    avoidWidowAndOrphanSuggested: bool
    shadingSuggestionState: ShadingSuggestionState
    pageBreakBeforeSuggested: bool


class SuggestedParagraphStyle(TypedDict):
    paragraphStyle: ParagraphStyle
    paragraphStyleSuggestionState: ParagraphStyleSuggestionState


class Bullet(TypedDict):
    listId: str
    nestingLevel: int
    textStyle: TextStyle


class BulletSuggestionState(TypedDict):
    listIdSuggested: bool
    nestingLevelSuggested: bool
    textStyleSuggestionState: TextStyleSuggestionState


class SuggestedBullet(TypedDict):
    bullet: Bullet
    bulletSuggestionState: BulletSuggestionState


class ObjectReferences(TypedDict):
    objectIds: list[str]


class Paragraph(TypedDict):
    elements: list[ParagraphElement]
    paragraphStyle: ParagraphStyle
    suggestedParagraphStyleChanges: dict[str, SuggestedParagraphStyle]
    bullet: Bullet
    suggestedBulletChanges: dict[str, SuggestedBullet]
    positionedObjectIds: list[str]
    suggestedPositionedObjectIdsChanges: dict[str, ObjectReferences]


class StructuralElementBase(TypedDict):
    startIndex: int
    endIndex: int


class SectionColumnProperties(TypedDict):
    width: Dimension
    paddingEnd: Dimension


ColumnSeparatorStyle = Literal["COLUMN_SEPARATOR_STYLE_UNSPECIFIED", "NONE", "BETWEEN_EACH_COLUMN"]
SectionType = Literal["SECTION_TYPE_UNSPECIFIED", "CONTINUOUS", "NEXT_PAGE"]


class SectionStyle(TypedDict):
    columnProperties: list[SectionColumnProperties]
    columnSeparatorStyle: ColumnSeparatorStyle
    contentDirection: ContentDirection
    marginTop: Dimension
    marginBottom: Dimension
    marginLeft: Dimension
    marginRight: Dimension
    marginHeader: Dimension
    marginFooter: Dimension
    sectionType: SectionType
    defaultHeaderId: str
    defaultFooterId: str
    firstPageHeaderId: str
    firstPageFooterId: str
    evenPageHeaderId: str
    evenPageFooterId: str
    useFirstPageHeaderFooter: bool
    pageNumberStart: int


class SectionBreak(TypedDict):
    suggestedInsertionIds: list[str]
    suggestedDeletionIds: list[str]
    sectionStyle: SectionStyle


class TableCellStyle(TypedDict):
    rowSpan: int
    columnSpan: int
    backgroundColor: OptionalColor
    borderLeft: ParagraphBorder
    borderRight: ParagraphBorder
    borderTop: ParagraphBorder
    borderBottom: ParagraphBorder
    paddingLeft: Dimension
    paddingRight: Dimension
    paddingTop: Dimension
    paddingBottom: Dimension
    contentAlignment: ContentAlignment


class TableCellStyleSuggestionState(TypedDict):
    rowSpanSuggested: bool
    columnSpanSuggested: bool
    backgroundColorSuggested: bool
    borderLeftSuggested: bool
    borderRightSuggested: bool
    borderTopSuggested: bool
    borderBottomSuggested: bool
    paddingLeftSuggested: bool
    paddingRightSuggested: bool
    paddingTopSuggested: bool
    paddingBottomSuggested: bool
    contentAlignmentSuggested: bool


class SuggestedTableCellStyle(TypedDict):
    tableCellStyle: TableCellStyle
    tableCellStyleSuggestionState: TableCellStyleSuggestionState


class TableCell(TypedDict):
    startIndex: int
    endIndex: int
    content: list[StructuralElementBase]  # currently underneath
    tableCellStyle: TableCellStyle
    suggestedInsertionIds: list[str]
    suggestedDeletionIds: list[str]
    suggestedTableCellStyleChanges: dict[str, SuggestedTableCellStyle]


class TableRowStyle(TypedDict):
    minRowHeight: Dimension
    tableHeader: bool
    preventOverflow: bool


class TableRowSuggestionsState(TypedDict):
    minRowHeightSuggested: bool


class SuggestedTableRowStyle(TypedDict):
    tableRowStyle: TableRowStyle
    tableRowStyleSuggestionState: TableRowSuggestionsState


class TableRow(TypedDict):
    startIndex: int
    endIndex: int
    tableCells: list[TableCell]
    suggestedInsertionIds: list[str]
    suggestedDeletionIds: list[str]
    tableRowStyle: TableRowStyle
    suggestedTableRowStyleChanges: dict[str, SuggestedTableRowStyle]


class TableColumnProperties(TypedDict):
    widthType: WidthType
    width: Dimension


class TableStyle(TypedDict):
    tableColumnProperties: list[TableColumnProperties]


class Table(TypedDict):
    rows: int
    columns: int
    tableRows: list[TableRow]
    suggestedInsertionIds: list[str]
    suggestedDeletionIds: list[str]
    tableStyle: TableStyle


class TableOfContents(TypedDict):
    content: list[StructuralElementBase]  # currently underneath
    suggestedInsertionIds: list[str]
    suggestedDeleteionIds: list[str]


class StructuralElement(StructuralElementBase, total=False):
    paragraph: Paragraph
    sectionBreak: SectionBreak
    table: Table
    tableOfContents: TableOfContents


class Body(TypedDict):
    content: list[StructuralElement]


class Header(TypedDict):
    headerId: str
    content: list[StructuralElement]


class Footer(TypedDict):
    footerId: str
    content: list[StructuralElement]


class Footnote(TypedDict):
    footnoteId: str
    content: list[StructuralElement]


class Background(TypedDict):
    color: OptionalColor


class Size(TypedDict):
    width: Dimension
    height: Dimension


class DocumentStyle(TypedDict):
    background: Background
    defaultHeaderId: str
    defaultFooterId: str
    evenPageHeaderId: str
    evenPageFooterId: str
    firstPageHeaderId: str
    firstPageFooterId: str
    useFirstPageHeaderFooter: bool
    useEvenPageHeaderFooter: bool
    pageNumberStart: int
    marginTop: Dimension
    marginBottom: Dimension
    marginLeft: Dimension
    marginRight: Dimension
    pageSize: Size
    marginHeader: Dimension
    marginFooter: Dimension
    useCustomHeaderFooterMargins: bool


class BackgroundSuggestionState(TypedDict):
    backgroundColorSuggested: bool


class SizeSuggestionState(TypedDict):
    heightSuggested: bool
    widthSuggested: bool


class DocumentStyleSuggestionState(TypedDict):
    backgroundSuggestionState: dict[str, BackgroundSuggestionState]
    defaultHeaderIdSuggested: bool
    defaultFooterIdSuggested: bool
    evenPageHeaderIdSuggested: bool
    evenPageFooterIdSuggested: bool
    firstPageHeaderIdSuggested: bool
    firstPageFooterIdSuggested: bool
    useFirstPageHeaderFooterSuggested: bool
    useEvenPageHeaderFooterSuggested: bool
    pageNumberStartSuggested: bool
    marginTopSuggested: bool
    marginBottomSuggested: bool
    marginRightSuggested: bool
    marginLeftSuggested: bool
    pageSizeSuggestionState: dict[str, SizeSuggestionState]
    marginHeaderSuggested: bool
    marginFooterSuggested: bool
    useCustomHeaderFooterMarginsSuggested: bool


class SuggestedDocumentStyle(TypedDict):
    documentStyle: DocumentStyle
    documentStyleSuggestionState: dict[str, DocumentStyleSuggestionState]


class NamedStyle(TypedDict):
    namedStyleType: NamedStyleType
    paragraphStyle: ParagraphStyle
    textStyle: TextStyle


class NamedStyles(TypedDict):
    styles: list[NamedStyle]


class NamedStyleSuggestionState(TypedDict):
    namedStyleType: NamedStyleType
    textStyleSuggestionState: TextStyleSuggestionState
    paragraphStyleSuggestionState: ParagraphStyleSuggestionState


class NamedStylesSuggestionState(TypedDict):
    stylesSuggestionStates: list[NamedStyleSuggestionState]


class SuggestedNamedStyles(TypedDict):
    namedStyles: NamedStyles
    namedStylesSuggestionState: dict[str, NamedStylesSuggestionState]


BulletAlignment = Literal["BULLET_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"]


class NestingLevelBase(TypedDict):
    bulletAlignment: BulletAlignment
    glyphFormat: str
    indentFirstLine: Dimension
    indentStart: Dimension
    textStyle: TextStyle
    startNumber: int


GlyphType = Literal[
    "GLYPH_TYPE_UNSPECIFIED",
    "NONE",
    "DECIMAL",
    "ZERO_DECIMAL",
    "UPPER_ALPHA",
    "ALPHA",
    "UPPER_ROMAN",
    "ROMAN",
]


class NestingLevel(NestingLevelBase, total=False):
    glyphType: GlyphType
    glyphSymbol: str


class ListProperties(TypedDict):
    nestingLevels: list[NestingLevel]


class NestingLevelSuggestionState(TypedDict):
    bulletAlignmentSuggested: bool
    glyphTypeSuggested: bool
    glyphFormatSuggested: bool
    glyphSymbolSuggested: bool
    indentFirstLineSuggested: bool
    indentStartSuggested: bool
    textStyleSuggestionState: TextStyleSuggestionState
    startNumberSuggested: bool


class ListPropertiesSuggestionState(TypedDict):
    nestingLevelsSuggestionStates: list[NestingLevelSuggestionState]


class SuggestedListProperties(TypedDict):
    listProperties: ListProperties
    listPropertiesSuggestionState: ListPropertiesSuggestionState


class List(TypedDict):
    listProperties: ListProperties
    suggestedListPropertiesChanges: dict[str, SuggestedListProperties]
    suggestedInsertionId: str
    suggestedDeletionIds: list[str]


class Range(TypedDict):
    segmentId: str
    startIndex: int
    endIndex: int


class NamedRange(TypedDict):
    namedRangeId: str
    name: str
    ranges: list[Range]


class NamedRanges(TypedDict):
    name: str
    ranges: list[NamedRange]


SuggestionsViewMode = Literal[
    "DEFAULT_FOR_CURRENT_ACCESS",
    "SUGGESTION_INLINE",
    "PREVIEW_SUGGESTIONS_ACCEPTED",
    "PREVIEW_WITHOUT_SUGGESTIONS",
]

PropertyState = Literal["RENDERED", "NOT_RENDERED"]


class EmbeddedObjectBorder(TypedDict):
    color: OptionalColor
    width: Dimension
    dashStyle: DashStyle
    propertyState: PropertyState


class SheetsChartReference(TypedDict):
    spreadsheetId: str
    chartId: int


class LinkedContentReference(TypedDict, total=False):
    sheetsChartReference: SheetsChartReference


class EmbeddedObjectBase(TypedDict):
    title: str
    description: str
    embeddedObjectBorder: EmbeddedObjectBorder
    size: Size
    marginTop: Dimension
    marginBottom: Dimension
    marginLeft: Dimension
    marginRight: Dimension
    linkedContentReference: LinkedContentReference


class CropProperties(TypedDict):
    offsetBottom: float
    offsetLeft: float
    offsetRight: float
    offsetTop: float
    angle: float


class ImageProperties(TypedDict):
    contentUri: str
    sourceUri: str
    brightness: float
    contrast: float
    transparency: float
    cropProperties: CropProperties
    angle: float


class EmbeddedObject(EmbeddedObjectBase, total=False):
    embeddedDrawingProperties: dict[str, Union[str, float, int, bool]]
    imageProperties: ImageProperties


class InlineObjectProperties(TypedDict):
    embeddedObject: EmbeddedObject


class InlineObject(TypedDict):
    objectId: str
    inlineObjectProperties: InlineObjectProperties
    suggestedInlineObjectPropertiesChanges: dict[str, InlineObjectProperties]
    suggestedInsertionId: str
    suggestedDeletionIds: list[str]


PositionedObjectLayout = Literal[
    "POSITIONED_OBJECT_LAYOUT_UNSPECIFIED",
    "WRAP_TEXT",
    "BREAK_LEFT",
    "BREAK_RIGHT",
    "BREAK_LEFT_RIGHT",
    "IN_FRONT_OF_TEXT",
    "BEHIND_TEXT",
]


class PositionedObjectPositioning(TypedDict):
    layout: PositionedObjectLayout
    leftOffset: Dimension
    topOffset: Dimension


class PositionedObjectProperties(TypedDict):
    positioning: PositionedObjectPositioning
    embeddedObject: EmbeddedObject


class PositionedObjectPositioningSuggestionState(TypedDict):
    layoutSuggested: bool
    leftOffsetSuggested: bool
    topOffsetSuggested: bool


class CropPropertiesSuggestionState(TypedDict):
    offsetLeftSuggested: bool
    offsetRightSuggested: bool
    offsetTopSuggested: bool
    offsetBottomSuggested: bool
    angleSuggested: bool


class ImagePropertiesSuggestionState(TypedDict):
    contentUriSuggested: bool
    sourceUriSuggested: bool
    brightnessSuggested: bool
    contrastSuggested: bool
    transparencySuggested: bool
    cropPropertiesSuggestionState: CropPropertiesSuggestionState
    angleSuggested: bool


class EmbeddedObjectBorderSuggestionState(TypedDict):
    colorSuggested: bool
    widthSuggested: bool
    dashStyleSuggested: bool
    propertyStateSuggested: bool


class SheetsChartReferenceSuggestionState(TypedDict):
    spreadsheetIdSuggested: bool
    chartIdSuggested: bool


class LinkedContentReferenceSuggestionState(TypedDict):
    sheetsChartReferenceSuggested: SheetsChartReferenceSuggestionState


class EmbeddedObjectSuggestionState(TypedDict):
    embeddedDrawingPropertiesSuggestionsState: dict[str, Union[str, float, int, bool]]
    imagePropertiesSuggestionState: ImagePropertiesSuggestionState
    titleSuggested: bool
    descriptionSuggested: bool
    embeddedObjectBorderSuggestionState: EmbeddedObjectBorderSuggestionState
    sizeSuggestionState: SizeSuggestionState
    marginTopSuggested: bool
    marginBottomSuggested: bool
    marginLeftSuggested: bool
    marginRightSuggested: bool
    linkedContentReferenceSuggestionState: LinkedContentReferenceSuggestionState


class PositionedObjectPropertiesSuggestionState(TypedDict):
    positioningSuggestionState: PositionedObjectPositioningSuggestionState
    embeddedObjectSuggestionState: EmbeddedObjectSuggestionState


class SuggestedPositionedObjectProperties(TypedDict):
    positionedObjectProperties: PositionedObjectProperties
    positioningSuggestionState: PositionedObjectPropertiesSuggestionState


class PositionedObject(TypedDict):
    objectId: str
    positionedObjectProperties: PositionedObjectProperties
    suggestedPositionedObjectPropertiesChanges: dict[str, SuggestedPositionedObjectProperties]
    suggestedInsertionId: str
    suggestedDeletionIds: list[str]


class Document(TypedDict):
    """https://developers.google.com/docs/api/reference/rest/v1/documents#Document"""

    documentId: str
    title: str
    body: Body
    headers: dict[str, Header]
    footers: dict[str, Footer]
    footnotes: dict[str, Footnote]
    documentStyle: DocumentStyle
    suggestedDocumentStyleChanges: dict[str, SuggestedDocumentStyle]
    namedStyles: dict[str, NamedStyles]
    suggestedNamedStylesChanges: dict[str, SuggestedNamedStyles]
    lists: dict[str, List]
    namedRanges: dict[str, NamedRanges]
    revisionId: str
    suggestionsViewMode: SuggestionsViewMode
    inlineObjects: dict[str, InlineObject]
    positionedObjects: dict[str, PositionedObject]
