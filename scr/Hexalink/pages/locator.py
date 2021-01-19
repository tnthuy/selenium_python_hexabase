class LoginPage:
    input_email = "//input[@name='username']"
    input_password = " //input[@name='password']"
    btn_signin = "//button[@class='btn-main md-button md-ink-ripple']"
    lbl_error = "//div/ul[@class='login-error ng-scope']"
    link_forgotPassword = "//div[@class='forgot-passwd']"


class ForgotPasswordPage:
    input_emailForgot = "//input[@name='emailAddress']"
    btn_passwordReset = "//button[@class='btn-main md-button md-ink-ripple']"
    btn_passordResetDisabled = "//button[@class='btn-main md-button md-ink-ripple' and @disabled='disabled']"
    lbl_errorForgotpassword = "//div[@class='err-msg ng-binding layout-align-center-center flex']"
    lbl_errorEmailtemplate = "//div[@class='md-input-message-animation ng-binding ng-scope']"


class HomePage:
    header = "//*[@id='header']"
    iconLogout = "//div/a[@id='logoutBtnPro']"
    iconSetting = "//div[@id='workspace-settings']"

    # workspace
    dropbox_workpase = "//md-select"
    dropped_workspace = "//md-select[@aria-expanded='true']"
    list_workspace = "//md-select-menu/md-content/md-option"

    current_workspace = "//md-select-value/span/div[@class='md-text ng-binding']"

    create_workspace = "//*[@id='select_listbox_4']/div"
    name_workspace = "//input[@name='workspaceName']"
    btn_create = "//div[@class='custom-popup-centerer']//button[contains(@class,'btn-submit') and not(@disabled)]"

    # Project
    projects = "//md-tab-item"
    first_project = "//md-tab-item[1]"

    # delete workspace
    btn_Archive = "//button[@class='md-raised btn-cancel md-button']"
    input_Archive = "//input[contains(@class,'mat-input-element')]"
    btn_deleteArchive = "//button[@class='mat-button btn-submit custom-popup-button']"

    # update
    input_UpdateWorkpace = "//md-input-container/input[@name='ws_name']"
    btn_UpdateWorkpace = "//div[contains(@class,'ws-settings-dialog-footer')]/button[@class='btn-submit md-button']"

    # Workspace Administrator
    groupAndMember = "//div[@class='ws-settings-dialog']//md-tabs-canvas/md-pagination-wrapper/md-tab-item[2]"
    listGmailMember = "//tbodsy/tr/td[2]//div[@class='ng-binding']"
    workpaceSettings = "//div[@class='ws-settings-dialog']//md-tabs-canvas/md-pagination-wrapper/md-tab-item[1]"
    inputAdministrator = "//div[@class='md-chip-input-container ng-scope']//input"
    emaiAdministrator = "//li[@class='md-autocomplete-suggestion ng-scope']"
    lisMemberAdministrator = "//md-chip[@class='ng-scope']/div[@class='md-chip-remove-container ng-scope']"

    # Wrokspace and group
    btn_groupTree = "//md-menu/button[@class='md-icon-button md-button']"
    btn_AddNewGroup = "//div[contains(@class,'md-clickable')]//span[contains(text(),'Add new Group')]/.."
    btn_layoutSetting = "//div[contains(@class,'md-clickable')]//span[contains(text(),'Layout Settings')]/.."
    input_GroupName = "//input[@name='groupName']"
    input_GroupID = "//input[@name='projectId']"
    btn_createGroup = "//button[@class='md-raised btn-submit md-button md-ink-ripple']"
    btn_cancelGroup = "//button[@class='md-raised btn-cancel md-button md-ink-ripple']"
    listGroupName = "//li[@ng-repeat='group in group.childGroups']//div[@class='group-name-container ng-binding ng-scope']"
    listDragAndDropGroupTree = "//div[@class='group-drag-handle ng-scope angular-ui-tree-handle']"
    btn_saveLayoutSetting = "//button[@class='btn-submit md-button']"
    btn_cancelLayoutSetting = "//button[@class='btn-cancel md-button']"

#      # UserProfile
#     imgUserProfile = By.xpath("//div[@class='user-panel-info layout-align-start-center layout-row']") 
#     personalize = By.xpath("//ul[@class='_md-nav-bar-list']/li[2]") 
#     languages = By.xpath("//div[@class='setting-input']//md-select-value[@class='md-select-value']") 
#     languagesJapan = By.xpath("//md-option[@class='lang-option ng-scope md-ink-ripple md-focused']") 
#     languagesEnglish = By.xpath("//md-option[@class='lang-option ng-scope md-ink-ripple']") 
#     buttonLanguagesCancel = By.xpath("//button[@class='mat-button btn-cancel custom-popup-button']") 
#     buttonLanguagesOk = By.xpath("//button[@class='mat-button btn-submit custom-popup-button']") 
#     blackColor = By.xpath("//md-radio-group/md-radio-button[@value='black']") 
#     blackColorTrue = By.xpath("//md-radio-group/md-radio-button[@value='black' and @aria-checked='true']") 
#     grayColor = By.xpath("//md-radio-group/md-radio-button[@value='gray']") 
#     grayColorTrue = By.xpath("//md-radio-group/md-radio-button[@value='gray' and @aria-checked='true']") 
#     privilages = By.xpath("//li[@name='access_key']/button[contains(@class,'_md-nav-button')]") 
#     myAccess = By.xpath("//div[@class='user']/div[@class='key-name ng-binding']") 
#     passwordChange = By.xpath("//li[@name='ch_pass']/button[contains(@class,'_md-nav-button')]") 
#     oldPassword = By.xpath("//input[@formcontrolname='oldPassword']") 
#     newPassword = By.xpath("//input[@formcontrolname='newPassword']") 
#     cofirmPassword = By.xpath("//input[@formcontrolname='confirmationPassword']") 
#     buttonSavePasswordChange = By.xpath("//button[@class='btn-submit md-button mat-button']") 
#      
#     
# 
# 
# class ProjectPage:
#     project_left_menu_display = By.xpath("//*[@id=\"col\"]/left-menu/div[@aria-hidden='false']") 
#     datastores_edit_menu = By.xpath("//*[@id=\"dataStoreEditMenu\"]") 
#     datastores_popup = By.xpath("//body/div/md-menu-content") 
#     create_new_database = By.xpath("//span[contains(text(), 'Create a new Database')]") 
# 
#      create_with_use_template = By.xpath("//button/span[contains(text(),'Use Template')]") 
#      create_with_make_from_import = By.xpath("//button/span[contains(text(),'Make From Import')]") 
#      create_with_link_external = By.xpath("//button/span[contains(text(),'Link External')]") 
# 
#      template_type_minimum_template = By.xpath("//div[contains(text(),'Minimum Template')]/..") 
#      template_type_todo_list_sample = By.xpath("//div[contains(text(),'ToDo List Sample')]/..") 
#      template_type_sync_group_database = By
#             .xpath("//div[contains(text(),'Sync Group Database')]/..") 
# 
#      btn_add_a_database_not_disabled = By
#             .xpath("//button[not(@disabled='disabled')]/span[contains(text(),'Add a Database')]") 
# 
#      btn_add_a_database = By.xpath("//button/span[contains(text(),'Add a Database')]")
