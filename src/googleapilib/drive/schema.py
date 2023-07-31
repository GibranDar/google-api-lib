from typing import TypedDict, Optional, Union


class Thumbnail(TypedDict):
    image: str
    mimeType: str


class User(TypedDict):
    displayName: str
    kind: str
    me: bool
    permissionId: str
    emailAddress: str
    photoLink: str


class PermissionDetail(TypedDict):
    permissionType: str
    inheritedFrom: str
    role: str
    inherited: bool


class TeamDrivePermissionDetail(TypedDict):
    teamDrivePermissionType: str
    inheritedFrom: str
    role: str
    inherited: bool


class Permission(TypedDict):
    id: str
    displayName: str
    type: str
    kind: str
    permissionDetails: list[PermissionDetail]
    photoLink: str
    emailAddress: str
    role: str
    allowFileDiscovery: bool
    domain: str
    expirationTime: str
    teamDrivePermissionDetails: list[TeamDrivePermissionDetail]
    deleted: bool
    view: str
    pendingOwner: bool


class Field(TypedDict):
    kind: str
    id: str
    valueType: str
    dateString: list[str]
    integer: list[str]
    selection: list[str]
    text: list[str]
    user: list[User]


class Label(TypedDict):
    id: str
    revisionId: str
    kind: str
    fields: dict[str, Field]


class LabelInfo(TypedDict):
    labels: list[Label]


class ContentHints(TypedDict):
    indexableText: str
    thumbnail: Thumbnail


class Capabilities(TypedDict):
    canChangeViewersCanCopyContent: bool
    canMoveChildrenOutOfDrive: bool
    canReadDrive: bool
    canEdit: bool
    canCopy: bool
    canComment: bool
    canAddChildren: bool
    canDelete: bool
    canDownload: bool
    canListChildren: bool
    canRemoveChildren: bool
    canRename: bool
    canTrash: bool
    canReadRevisions: bool
    canReadTeamDrive: bool
    canMoveTeamDriveItem: bool
    canChangeCopyRequiresWriterPermission: bool
    canMoveItemIntoTeamDrive: bool
    canUntrash: bool
    canModifyContent: bool
    canMoveItemWithinTeamDrive: bool
    canMoveItemOutOfTeamDrive: bool
    canDeleteChildren: bool
    canMoveChildrenOutOfTeamDrive: bool
    canMoveChildrenWithinTeamDrive: bool
    canTrashChildren: bool
    canMoveItemOutOfDrive: bool
    canAddMyDriveParent: bool
    canRemoveMyDriveParent: bool
    canMoveItemWithinDrive: bool
    canShare: bool
    canMoveChildrenWithinDrive: bool
    canModifyContentRestriction: bool
    canAddFolderFromAnotherDrive: bool
    canChangeSecurityUpdateEnabled: bool
    canAcceptOwnership: bool
    canReadLabels: bool
    canModifyLabels: bool
    canModifyEditorContentRestriction: bool
    canModifyOwnerContentRestriction: bool
    canRemoveContentRestriction: bool


class Location(TypedDict):
    latitude: float
    longitude: float
    altitude: float


class ImageMediaMetadata(TypedDict):
    flashUsed: bool
    meteringMode: str
    sensor: str
    exposureMode: str
    colorSpace: str
    whiteBalance: str
    width: int
    height: int
    location: Location
    rotation: int
    time: str
    cameraMake: str
    cameraModel: str
    exposureTime: float
    aperture: float
    focalLength: float
    isoSpeed: int
    exposureBias: float
    maxApertureValue: float
    subjectDistance: int
    lens: str


class VideoMediaMetadata(TypedDict):
    width: int
    height: int
    durationMillis: str


class ShortcutDetails(TypedDict):
    targetId: str
    targetMimeType: str
    targetResourceKey: str


class ContentRestriction(TypedDict):
    readOnly: bool
    reason: str
    restrictingUser: User
    restrictionTime: str
    type: str


class LinkShareMetadata(TypedDict):
    securityUpdateEligible: bool
    securityUpdateEnabled: bool


class File(TypedDict, total=False):
    """https://developers.google.com/drive/api/reference/rest/v3/files#File"""

    kind: str
    driveId: str
    fileExtension: str
    copyRequiresWriterPermission: bool
    md5Checksum: str
    contentHints: ContentHints
    writersCanShare: bool
    viewedByMe: bool
    mimeType: str
    exportLinks: dict[str, str]
    parents: list[str]
    thumbnailLink: str
    iconLink: str
    shared: bool
    lastModifyingUser: Optional[User]
    owners: list[User]
    headRevisionId: str
    sharingUser: Optional[User]
    webViewLink: str
    webContentLink: str
    size: str
    viewersCanCopyContent: bool
    permissions: list[Permission]
    hasThumbnail: bool
    spaces: list[str]
    folderColorRgb: str
    id: str
    name: str
    description: str
    starred: bool
    trashed: bool
    explicitlyTrashed: bool
    createdTime: str
    modifiedTime: str
    modifiedByMeTime: str
    viewedByMeTime: str
    sharedWithMeTime: str
    quotaBytesUsed: str
    version: str
    originalFilename: str
    ownedByMe: bool
    fullFileExtension: str
    properties: dict[str, Union[str, int, float, bool]]
    appProperties: dict[str, Union[str, int, float, bool]]
    isAppAuthorized: bool
    teamDriveId: str
    capabilities: Capabilities
    hasAugmentedPermissions: bool
    trashingUser: Optional[User]
    thumbnailVersion: str
    trashedTime: str
    modifiedByMe: bool
    permissionIds: list[str]
    imageMediaMetadata: ImageMediaMetadata
    videoMediaMetadata: VideoMediaMetadata
    shortcutDetails: ShortcutDetails
    contentRestrictions: list[ContentRestriction]
    resourceKey: str
    linkShareMetadata: LinkShareMetadata
    labelInfo: LabelInfo
    sha1Checksum: str
    sha256Checksum: str
