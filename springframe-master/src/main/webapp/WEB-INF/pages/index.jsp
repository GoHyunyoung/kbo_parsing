<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <title>KBO Article Generator | Timeline</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/resources/assets/bootstrap-3.3.4/css/bootstrap.min.css">

    <link href="http://fonts.googleapis.com/css?family=Open+Sans:400,300,600,700&subset=all" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/simple-line-icons/simple-line-icons.min.css" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/uniform/css/uniform.default.css" rel="stylesheet" type="text/css">
    <!-- END GLOBAL MANDATORY STYLES -->
    <!-- BEGIN PAGE LEVEL STYLES -->
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/admin/pages/css/timeline.css" rel="stylesheet" type="text/css"/>
    <!-- END PAGE LEVEL STYLES -->
    <!-- BEGIN THEME STYLES -->
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/global/css/components.css" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/global/css/plugins.css" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/admin/layout3/css/layout.css" rel="stylesheet" type="text/css">
    <link href="/resources/assets/metronic_v3.3.0/theme/assets/admin/layout3/css/themes/default.css" rel="stylesheet" type="text/css" id="style_color">
    <link href="/resources/assets/css/custom.css" rel="stylesheet" type="text/css">
    <!-- END THEME STYLES -->

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="/resources/assets/bootstrap-3.3.4/js/bootstrap.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.1.0.min.js"></script>
    <script type="text/javascript" src="/resources/assets/javascript/infinite_scrpll.js"></script>
    <script type="text/javascript" src="/resources/assets/javascript/search.js"></script>
</head>

<body>
<!-- BEGIN HEADER -->
<div class="page-header">
    <!-- BEGIN HEADER TOP -->
    <div class="page-header-top">
        <div class="container">
            <!-- BEGIN LOGO -->
            <div class="page-logo">
                <a href="/"><img src="/resources/images/logo-default.png" alt="logo" class="logo-default"></a>
            </div>
            <!-- END LOGO -->

        </div>
    </div>
    <!-- END HEADER TOP -->
    <!-- BEGIN HEADER MENU -->
    <div class="page-header-menu">
        <div class="container">
            <!-- BEGIN HEADER SEARCH BOX -->
            <form class="search-form" action="search" method="GET">
                <div class="input-group">
                    <input type="text" class="form-control" placeholder="Search" name="query">
                    <span class="input-group-btn">
					<a href="javascript:;" class="btn submit"><i class="icon-magnifier"></i></a>
					</span>
                </div>
            </form>
            <!-- END HEADER SEARCH BOX -->
            <!-- BEGIN MEGA MENU -->
            <!-- DOC: Apply "hor-menu-light" class after the "hor-menu" class below to have a horizontal menu with white background -->
            <!-- DOC: Remove data-hover="dropdown" and data-close-others="true" attributes below to disable the dropdown opening on mouse hover -->
            <div class="hor-menu ">
                <ul class="nav navbar-nav">
                    <li>
                        <a href="index.html">Dashboard</a>
                    </li>
                    <li class="menu-dropdown mega-menu-dropdown ">
                        <a data-hover="megamenu-dropdown" data-close-others="true" data-toggle="dropdown" href="javascript:;" class="dropdown-toggle">
                            Features <i class="fa fa-angle-down"></i>
                        </a>
                        <ul class="dropdown-menu" style="min-width: 710px">
                            <li>
                                <div class="mega-menu-content">
                                    <div class="row">
                                        <div class="col-md-4">
                                            <ul class="mega-menu-submenu">
                                                <li>
                                                    <h3>eCommerce</h3>
                                                </li>
                                                <li>
                                                    <a href="ecommerce_index.html" class="iconify">
                                                        <i class="icon-home"></i>
                                                        eCommerce </a>
                                                </li>
                                                <li>
                                                    <a href="ecommerce_orders.html" class="iconify">
                                                        <i class="icon-basket"></i>
                                                        Manage Orders </a>
                                                </li>
                                                <li>
                                                    <a href="ecommerce_orders_view.html" class="iconify">
                                                        <i class="icon-tag"></i>
                                                        Order View </a>
                                                </li>
                                                <li>
                                                    <a href="ecommerce_products.html" class="iconify">
                                                        <i class="icon-handbag"></i>
                                                        Manage Products </a>
                                                </li>
                                                <li>
                                                    <a href="ecommerce_products_edit.html" class="iconify">
                                                        <i class="icon-pencil"></i>
                                                        Product Edit </a>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="col-md-4">
                                            <ul class="mega-menu-submenu">
                                                <li>
                                                    <h3>Layouts</h3>
                                                </li>
                                                <li>
                                                    <a href="layout_fluid.html" class="iconify">
                                                        <i class="icon-cursor-move"></i>
                                                        Fluid Layout </a>
                                                </li>
                                                <li>
                                                    <a href="layout_mega_menu_fixed.html" class="iconify">
                                                        <i class="icon-pin"></i>
                                                        Fixed Mega Menu </a>
                                                </li>
                                                <li>
                                                    <a href="layout_top_bar_fixed.html" class="iconify">
                                                        <i class="icon-bar-chart"></i>
                                                        Fixed Top Bar </a>
                                                </li>
                                                <li>
                                                    <a href="layout_light_header.html" class="iconify">
                                                        <i class="icon-paper-plane"></i>
                                                        Light Header Dropdowns </a>
                                                </li>
                                                <li>
                                                    <a href="layout_blank_page.html" class="iconify">
                                                        <i class="icon-doc"></i>
                                                        Blank Page Layout </a>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="col-md-4">
                                            <ul class="mega-menu-submenu">
                                                <li>
                                                    <h3>More Layouts</h3>
                                                </li>
                                                <li>
                                                    <a href="layout_click_dropdowns.html" class="iconify">
                                                        <i class="icon-speech"></i>
                                                        Click vs. Hover Dropdowns </a>
                                                </li>
                                                <li>
                                                    <a href="layout_fontawesome_icons.html" class="iconify">
                                                        <i class="icon-link"></i>
                                                        Layout with Fontawesome </a>
                                                </li>
                                                <li>
                                                    <a href="layout_glyphicons.html" class="iconify">
                                                        <i class="icon-settings"></i>
                                                        Layout with Glyphicon </a>
                                                </li>
                                                <li>
                                                    <a href="layout_language_bar.html" class="iconify">
                                                        <i class="icon-globe"></i>
                                                        Language Switch Bar </a>
                                                </li>
                                                <li>
                                                    <a href="layout_disabled_menu.html" class="iconify">
                                                        <i class=" icon-lock"></i>
                                                        Disabled Menu Links </a>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </li>
                    <li class="menu-dropdown mega-menu-dropdown mega-menu-full ">
                        <a data-hover="megamenu-dropdown" data-close-others="true" data-toggle="dropdown" href="javascript:;" class="dropdown-toggle">
                            UI Components <i class="fa fa-angle-down"></i>
                        </a>
                        <ul class="dropdown-menu">
                            <li>
                                <div class="mega-menu-content">
                                    <div class="row">
                                        <div class="col-md-3">
                                            <ul class="mega-menu-submenu">
                                                <li>
                                                    <h3>UI Components</h3>
                                                </li>
                                                <li>
                                                    <a href="ui_general.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        General </a>
                                                </li>
                                                <li>
                                                    <a href="ui_buttons.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Buttons </a>
                                                </li>
                                                <li>
                                                    <a href="ui_icons.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Font Icons </a>
                                                </li>
                                                <li>
                                                    <a href="ui_colors.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Flat UI Colors </a>
                                                </li>
                                                <li>
                                                    <a href="ui_typography.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Typography </a>
                                                </li>
                                                <li>
                                                    <a href="ui_tabs_accordions_navs.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Tabs, Accordions &amp; Navs </a>
                                                </li>
                                                <li>
                                                    <a href="ui_tree.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Tree View </a>
                                                </li>
                                                <li>
                                                    <a href="ui_page_progress_style_1.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Page Progress Bar <span class="badge badge-roundless badge-warning">new</span></a>
                                                </li>
                                                <li>
                                                    <a href="ui_blockui.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Block UI </a>
                                                </li>
                                                <li>
                                                    <a href="ui_notific8.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Notific8 Notifications </a>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="col-md-3">
                                            <ul class="mega-menu-submenu">
                                                <li>
                                                    <h3>More UI Components</h3>
                                                </li>
                                                <li>
                                                    <a href="ui_toastr.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Toastr Notifications </a>
                                                </li>
                                                <li>
                                                    <a href="ui_alert_dialog_api.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Alerts &amp; Dialogs API <span class="badge badge-roundless badge-danger">new</span></a>
                                                </li>
                                                <li>
                                                    <a href="ui_session_timeout.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Session Timeout </a>
                                                </li>
                                                <li>
                                                    <a href="ui_idle_timeout.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        User Idle Timeout </a>
                                                </li>
                                                <li>
                                                    <a href="ui_modals.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Modals </a>
                                                </li>
                                                <li>
                                                    <a href="ui_extended_modals.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Extended Modals </a>
                                                </li>
                                                <li>
                                                    <a href="ui_tiles.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Tiles </a>
                                                </li>
                                                <li>
                                                    <a href="ui_datepaginator.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Date Paginator </a>
                                                </li>
                                                <li>
                                                    <a href="ui_nestable.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Nestable List </a>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="col-md-3">
                                            <ul class="mega-menu-submenu">
                                                <li>
                                                    <h3>Form Stuff</h3>
                                                </li>
                                                <li>
                                                    <a href="form_controls.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Form Controls </a>
                                                </li>
                                                <li>
                                                    <a href="form_layouts.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Form Layouts </a>
                                                </li>
                                                <li>
                                                    <a href="form_editable.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Form X-editable <span class="badge badge-roundless badge-success">new</span></a>
                                                </li>
                                                <li>
                                                    <a href="form_wizard.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Form Wizard </a>
                                                </li>
                                                <li>
                                                    <a href="form_validation.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Form Validation </a>
                                                </li>
                                                <li>
                                                    <a href="form_image_crop.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Image Cropping </a>
                                                </li>
                                                <li>
                                                    <a href="form_fileupload.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Multiple File Upload </a>
                                                </li>
                                                <li>
                                                    <a href="form_dropzone.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Dropzone File Upload </a>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="col-md-3">
                                            <ul class="mega-menu-submenu">
                                                <li>
                                                    <h3>Form Components</h3>
                                                </li>
                                                <li>
                                                    <a href="components_pickers.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Pickers </a>
                                                </li>
                                                <li>
                                                    <a href="components_dropdowns.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Custom Dropdowns </a>
                                                </li>
                                                <li>
                                                    <a href="components_form_tools.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Form Tools </a>
                                                </li>
                                                <li>
                                                    <a href="components_editors.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Markdown &amp; WYSIWYG Editors </a>
                                                </li>
                                                <li>
                                                    <a href="components_ion_sliders.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Ion Range Sliders </a>
                                                </li>
                                                <li>
                                                    <a href="components_noui_sliders.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        NoUI Range Sliders </a>
                                                </li>
                                                <li>
                                                    <a href="components_jqueryui_sliders.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        jQuery UI Sliders </a>
                                                </li>
                                                <li>
                                                    <a href="components_knob_dials.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Knob Circle Dials </a>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </li>
                    <li class="menu-dropdown classic-menu-dropdown ">
                        <a data-hover="megamenu-dropdown" data-close-others="true" data-toggle="dropdown" href="javascript:;" class="">
                            Extra <i class="fa fa-angle-down"></i>
                        </a>
                        <ul class="dropdown-menu pull-left">
                            <li class=" dropdown-submenu">
                                <a href=":;">
                                    <i class="icon-briefcase"></i>
                                    Data Tables </a>
                                <ul class="dropdown-menu">
                                    <li class=" ">
                                        <a href="table_basic.html">
                                            Basic Datatables </a>
                                    </li>
                                    <li class=" ">
                                        <a href="table_responsive.html">
                                            Responsive Datatables </a>
                                    </li>
                                    <li class=" ">
                                        <a href="table_managed.html">
                                            Managed Datatables </a>
                                    </li>
                                    <li class=" ">
                                        <a href="table_editable.html">
                                            Editable Datatables </a>
                                    </li>
                                    <li class=" ">
                                        <a href="table_advanced.html">
                                            Advanced Datatables </a>
                                    </li>
                                    <li class=" ">
                                        <a href="table_ajax.html">
                                            Ajax Datatables </a>
                                    </li>
                                </ul>
                            </li>
                            <li class=" dropdown-submenu">
                                <a href=":;">
                                    <i class="icon-wallet"></i>
                                    Portlets </a>
                                <ul class="dropdown-menu">
                                    <li class=" ">
                                        <a href="portlet_general.html">
                                            General Portlets </a>
                                    </li>
                                    <li class=" ">
                                        <a href="portlet_general2.html">
                                            New Portlets #1 <span class="badge badge-roundless badge-danger">new</span>
                                        </a>
                                    </li>
                                    <li class=" ">
                                        <a href="portlet_general3.html">
                                            New Portlets #2 <span class="badge badge-roundless badge-danger">new</span>
                                        </a>
                                    </li>
                                    <li class=" ">
                                        <a href="portlet_ajax.html">
                                            Ajax Portlets </a>
                                    </li>
                                    <li class=" ">
                                        <a href="portlet_draggable.html">
                                            Draggable Portlets </a>
                                    </li>
                                </ul>
                            </li>
                            <li class=" dropdown-submenu">
                                <a href=":;">
                                    <i class="icon-pointer"></i>
                                    Maps </a>
                                <ul class="dropdown-menu">
                                    <li class=" ">
                                        <a href="maps_google.html">
                                            Google Maps </a>
                                    </li>
                                    <li class=" ">
                                        <a href="maps_vector.html">
                                            Vector Maps </a>
                                    </li>
                                </ul>
                            </li>
                            <li class=" ">
                                <a href="charts.html">
                                    <i class="icon-bar-chart"></i>
                                    Visual Charts </a>
                            </li>
                            <li class="divider">
                            </li>
                            <li class=" dropdown-submenu">
                                <a href=":;">
                                    <i class="icon-puzzle"></i>
                                    Multi Level </a>
                                <ul class="dropdown-menu">
                                    <li class=" ">
                                        <a href="#">
                                            <i class="icon-settings"></i>
                                            Item 1 </a>
                                    </li>
                                    <li class=" ">
                                        <a href="#">
                                            <i class="icon-user"></i>
                                            Item 2 </a>
                                    </li>
                                    <li class=" ">
                                        <a href="#">
                                            <i class="icon-globe"></i>
                                            Item 3 </a>
                                    </li>
                                    <li class=" dropdown-submenu">
                                        <a href="#">
                                            <i class="icon-folder"></i>
                                            Sub Items </a>
                                        <ul class="dropdown-menu">
                                            <li class=" ">
                                                <a href="#">
                                                    Item 1 </a>
                                            </li>
                                            <li class=" ">
                                                <a href="#">
                                                    Item 2 </a>
                                            </li>
                                            <li class=" ">
                                                <a href="#">
                                                    Item 3 </a>
                                            </li>
                                            <li class=" ">
                                                <a href="#">
                                                    Item 4 </a>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class=" ">
                                        <a href="#">
                                            <i class="icon-share"></i>
                                            Item 4 </a>
                                    </li>
                                    <li class=" ">
                                        <a href="#">
                                            <i class="icon-bar-chart"></i>
                                            Item 5 </a>
                                    </li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                    <li class="menu-dropdown mega-menu-dropdown mega-menu-full active">
                        <a data-hover="megamenu-dropdown" data-close-others="true" data-toggle="dropdown" href="javascript:;" class="dropdown-toggle">
                            Pages <i class="fa fa-angle-down"></i>
                        </a>
                        <ul class="dropdown-menu">
                            <li>
                                <div class="mega-menu-content">
                                    <div class="row">
                                        <div class="col-md-3">
                                            <ul class="mega-menu-submenu">
                                                <li>
                                                    <h3>User Pages</h3>
                                                </li>
                                                <li>
                                                    <a href="page_todo.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Todo &amp; Tasks <span class="badge badge-danger">4</span></a>
                                                </li>
                                                <li>
                                                    <a href="inbox.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        User Inbox <span class="badge badge-success">4</span></a>
                                                </li>
                                                <li>
                                                    <a href="page_calendar.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        User Calendar <span class="badge badge-warning">14</span></a>
                                                </li>
                                                <li>
                                                    <a href="extra_profile.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        User Profile </a>
                                                </li>
                                                <li>
                                                    <a href="extra_lock.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Lock Screen </a>
                                                </li>
                                                <li>
                                                    <a href="login.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Login Form 1 </a>
                                                </li>
                                                <li>
                                                    <a href="login_soft.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Login Form 2 </a>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="col-md-3">
                                            <ul class="mega-menu-submenu">
                                                <li>
                                                    <h3>General Pages</h3>
                                                </li>
                                                <li>
                                                    <a href="extra_faq.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        FAQ Page </a>
                                                </li>
                                                <li>
                                                    <a href="page_portfolio.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Portfolio </a>
                                                </li>
                                                <li class="active">
                                                    <a href="page_timeline.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Timeline <span class="badge badge-info">4</span></a>
                                                </li>
                                                <li>
                                                    <a href="page_coming_soon.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Coming Soon </a>
                                                </li>
                                                <li>
                                                    <a href="extra_invoice.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Invoice </a>
                                                </li>
                                                <li>
                                                    <a href="page_blog.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Blog </a>
                                                </li>
                                                <li>
                                                    <a href="page_blog_item.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Blog Post </a>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="col-md-3">
                                            <ul class="mega-menu-submenu">
                                                <li>
                                                    <h3>Custom Pages</h3>
                                                </li>
                                                <li>
                                                    <a href="page_news.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        News <span class="badge badge-success">9</span></a>
                                                </li>
                                                <li>
                                                    <a href="page_news_item.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        News View </a>
                                                </li>
                                                <li>
                                                    <a href="page_about.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        About Us </a>
                                                </li>
                                                <li>
                                                    <a href="page_contact.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Contact Us </a>
                                                </li>
                                                <li>
                                                    <a href="extra_search.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Search Results </a>
                                                </li>
                                                <li>
                                                    <a href="extra_pricing_table.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Pricing Tables </a>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="col-md-3">
                                            <ul class="mega-menu-submenu">
                                                <li>
                                                    <h3>Miscellaneous</h3>
                                                </li>
                                                <li>
                                                    <a href="extra_404_option1.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        404 Page Option 1 </a>
                                                </li>
                                                <li>
                                                    <a href="extra_404_option2.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        404 Page Option 2 </a>
                                                </li>
                                                <li>
                                                    <a href="extra_404_option3.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        404 Page Option 3 </a>
                                                </li>
                                                <li>
                                                    <a href="extra_500_option1.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        500 Page Option 1 </a>
                                                </li>
                                                <li>
                                                    <a href="extra_500_option2.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        500 Page Option 2 </a>
                                                </li>
                                                <li>
                                                    <a href="email_newsletter.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        Newsletter Email Template </a>
                                                </li>
                                                <li>
                                                    <a href="email_system.html">
                                                        <i class="fa fa-angle-right"></i>
                                                        System Email Template </a>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </li>
                    <!-- begin: mega menu with custom content -->
                    <li class="menu-dropdown mega-menu-dropdown mega-menu-full hide">
                        <a data-hover="megamenu-dropdown" data-close-others="true" data-toggle="dropdown" href="javascript:;" class="dropdown-toggle">
                            Mega Menu <i class="fa fa-angle-down"></i>
                        </a>
                        <ul class="dropdown-menu">
                            <li>
                                <div class="mega-menu-content">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <div id="accordion" class="panel-group">
                                                <div class="panel panel-success">
                                                    <div class="panel-heading">
                                                        <h4 class="panel-title">
                                                            <a data-toggle="collapse" data-parent="#accordion" href="#collapseOne" class="collapsed">
                                                                Mega Menu Info #1 </a>
                                                        </h4>
                                                    </div>
                                                    <div id="collapseOne" class="panel-collapse in">
                                                        <div class="panel-body">
                                                            <p>
                                                                Metronic Mega Menu Works for fixed and responsive layout and has the facility to include (almost) any Bootstrap elements and jquery plugins.
                                                            </p>
                                                            <p>
                                                                Duis mollis, est non commodo luctus, nisi erat mattis consectetur purus sit amet porttitor ligula. nisi erat mattis consectetur purus
                                                            </p>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="panel panel-danger">
                                                    <div class="panel-heading">
                                                        <h4 class="panel-title">
                                                            <a data-toggle="collapse" data-parent="#accordion" href="#collapseTwo" class="collapsed">
                                                                Mega Menu Info #2 </a>
                                                        </h4>
                                                    </div>
                                                    <div id="collapseTwo" class="panel-collapse collapse">
                                                        <div class="panel-body">
                                                            <p>
                                                                Metronic Mega Menu Works for fixed and responsive layout and has the facility to include (almost) any Bootstrap elements and jquery plugins.
                                                            </p>
                                                            <p>
                                                                Duis mollis, est non commodo luctus, nisi erat mattis consectetur purus sit amet porttitor ligula. nisi erat mattis consectetur purus
                                                            </p>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="panel panel-info">
                                                    <div class="panel-heading">
                                                        <h4 class="panel-title">
                                                            <a data-toggle="collapse" data-parent="#accordion" href="#collapseThree">
                                                                Mega Menu Info #3 </a>
                                                        </h4>
                                                    </div>
                                                    <div id="collapseThree" class="panel-collapse collapse">
                                                        <div class="panel-body">
                                                            <p>
                                                                Metronic Mega Menu Works for fixed and responsive layout and has the facility to include (almost) any Bootstrap elements and jquery plugins.
                                                            </p>
                                                            <p>
                                                                Duis mollis, est non commodo luctus, nisi erat mattis consectetur purus sit amet porttitor ligula. nisi erat mattis consectetur purus
                                                            </p>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-md-6">
                                            <div class="portlet light">
                                                <div class="portlet-title">
                                                    <div class="caption">
                                                        <i class="fa fa-cogs font-red-sunglo"></i>
                                                        <span class="caption-subject font-red-sunglo bold uppercase">Notes</span>
                                                        <span class="caption-helper">notes samples...</span>
                                                    </div>
                                                    <div class="tools">
                                                        <a href="javascript:;" class="collapse">
                                                        </a>
                                                        <a href="#portlet-config" data-toggle="modal" class="config">
                                                        </a>
                                                        <a href="javascript:;" class="reload">
                                                        </a>
                                                        <a href="javascript:;" class="remove">
                                                        </a>
                                                    </div>
                                                </div>
                                                <div class="portlet-body">
                                                    <div class="note note-success">
                                                        <h4 class="block">Success! Some Header Goes Here</h4>
                                                        <p>
                                                            Duis mollis, est non commodo luctus, nisi erat mattis consectetur purus sit amet porttitor ligula, eget lacinia odio sem nec elit. Cras mattis consectetur purus sit amet fermentum.
                                                        </p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </li>
                    <!-- end: mega menu with custom content -->
                </ul>
            </div>
            <!-- END MEGA MENU -->
        </div>
    </div>
    <!-- END HEADER MENU -->
</div>
<!-- END HEADER -->
<!-- BEGIN PAGE CONTAINER -->
<div class="page-container">
    <!-- BEGIN PAGE HEAD -->
    <div class="page-head">
        <div class="container">
            <!-- BEGIN PAGE TITLE -->
            <div class="page-title">
                <h1>Timeline <small>Recent Article on the KBO  </small></h1>
            </div>
            <!-- END PAGE TITLE -->
        </div>
    </div>
    <!-- END PAGE HEAD -->
    <!-- BEGIN PAGE CONTENT -->
    <div class="page-content">
        <div class="container">
            <!-- BEGIN SAMPLE PORTLET CONFIGURATION MODAL FORM-->
            <div class="modal fade" id="portlet-config" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true"></button>
                            <h4 class="modal-title">Modal title</h4>
                        </div>
                        <div class="modal-body">
                            Widget settings form goes here
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn blue">Save changes</button>
                            <button type="button" class="btn default" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                    <!-- /.modal-content -->
                </div>
                <!-- /.modal-dialog -->
            </div>
            <!-- /.modal -->
            <!-- END SAMPLE PORTLET CONFIGURATION MODAL FORM-->
            <!-- BEGIN PAGE BREADCRUMB -->
            <ul class="page-breadcrumb breadcrumb">
                <li>
                    <a href="#">Home</a><i class="fa fa-circle"></i>
                </li>
                <li>
                    <a href="page_timeline.html">Pages</a>
                    <i class="fa fa-circle"></i>
                </li>
                <li class="active">
                    Timeline
                </li>
            </ul>
            <!-- END PAGE BREADCRUMB -->
            <!-- BEGIN PAGE CONTENT INNER -->

            <div class="portlet light">
                <div class="portlet-body">
                    <div class="row">
                        <div class="col-md-12">
                            <ul class="timeline">
                                <c:forEach var="i" begin="1" end="9" step="1">
                                    <li class=timeline>
                                        <div class="timeline-time">
                                            <c:choose>
                                                <c:when test="${articleList.get(i).date != articleList.get(i-1).date}">
                                                    <span class="time" style='color: #303a41'>${articleList.get(i).date}</span>
                                                </c:when>
                                            </c:choose>
                                        </div>
                                        <div class="timeline-icon">
                                        </div>
                                        <div class="timeline-body" data-name="${articleList.get(i).emblem}">
                                            <h2>${articleList.get(i).head}</h2>
                                            <div class="timeline-content">
                                                <img class="timeline-img pull-left" src=${String.format("/resources/images/emblem_image/emblemB_%s.png",articleList.get(i).emblem)} alt="${articleList.get(i).emblem}">
                                                    ${articleList.get(i).intro}
                                                <br/>
                                                    ${articleList.get(i).main}
                                            </div>
                                            <div class="timeline-footer">
                                                <a href="${articleList.get(i).url}" class="nav-link pull-right">
                                                    해당 경기 상세히 보러가기<i class="m-icon-swapright m-icon-white"></i>
                                                </a>
                                            </div>
                                        </div>
                                    </li>
                                </c:forEach>
                                <li id="getMoreArticle" align="center">
                                    <img src="/resources/images/page-loading.gif" id="loading-img" alt="Loading" width="180px" />
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <!-- END PAGE CONTENT INNER -->
        </div>
    </div>
    <!-- END PAGE CONTENT -->
</div>
<!-- END PAGE CONTAINER -->
<!-- BEGIN PRE-FOOTER -->
<div class="page-prefooter">
    <div class="container">
        <div class="row">
            <div class="col-md-3 col-sm-6 col-xs-12 footer-block">
                <h2>About</h2>
                <p>
                    Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam dolore.
                </p>
            </div>
            <div class="col-md-3 col-sm-6 col-xs12 footer-block">
                <h2>Subscribe Email</h2>
                <div class="subscribe-form">
                    <form action="#">
                        <div class="input-group">
                            <input type="text" placeholder="mail@email.com" class="form-control">
                            <span class="input-group-btn">
							<button class="btn" type="submit">Submit</button>
							</span>
                        </div>
                    </form>
                </div>
            </div>
            <div class="col-md-3 col-sm-6 col-xs-12 footer-block">
                <h2>Follow Us On</h2>
                <ul class="social-icons">
                    <li>
                        <a href="#" data-original-title="rss" class="rss"></a>
                    </li>
                    <li>
                        <a href="#" data-original-title="facebook" class="facebook"></a>
                    </li>
                    <li>
                        <a href="#" data-original-title="twitter" class="twitter"></a>
                    </li>
                    <li>
                        <a href="#" data-original-title="googleplus" class="googleplus"></a>
                    </li>
                    <li>
                        <a href="#" data-original-title="linkedin" class="linkedin"></a>
                    </li>
                    <li>
                        <a href="#" data-original-title="youtube" class="youtube"></a>
                    </li>
                    <li>
                        <a href="#" data-original-title="vimeo" class="vimeo"></a>
                    </li>
                </ul>
            </div>
            <div class="col-md-3 col-sm-6 col-xs-12 footer-block">
                <h2>Contacts</h2>
                <address class="margin-bottom-40">
                    Phone: 800 123 3456<br>
                    Email: <a href="mailto:info@metronic.com">info@metronic.com</a>
                </address>
            </div>
        </div>
    </div>
</div>
<!-- END PRE-FOOTER -->
<!-- BEGIN FOOTER -->
<div class="page-footer">
    <div class="container">
        2014 © Metronic. All Rights Reserved.
    </div>
</div>
<div class="scroll-to-top" style="display: none;">
    <i class="icon-arrow-up"></i>
</div>
<!-- END FOOTER -->
<!-- BEGIN JAVASCRIPTS(Load javascripts at bottom, this will reduce page load time) -->
<!-- BEGIN CORE PLUGINS -->
<!--[if lt IE 9]>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/respond.min.js"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/excanvas.min.js"></script>
<![endif]-->
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/jquery-1.11.0.min.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/jquery-migrate-1.2.1.min.js" type="text/javascript"></script>
<!-- IMPORTANT! Load jquery-ui-1.10.3.custom.min.js before bootstrap.min.js to fix bootstrap tooltip conflict with jquery ui tooltip -->
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/jquery-ui/jquery-ui-1.10.3.custom.min.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/bootstrap/js/bootstrap.min.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/bootstrap-hover-dropdown/bootstrap-hover-dropdown.min.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/jquery-slimscroll/jquery.slimscroll.min.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/jquery.blockui.min.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/jquery.cokie.min.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/plugins/uniform/jquery.uniform.min.js" type="text/javascript"></script>
<!-- END CORE PLUGINS -->
<script src="/resources/assets/metronic_v3.3.0/theme/assets/global/scripts/metronic.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/admin/layout3/scripts/layout.js" type="text/javascript"></script>
<script src="/resources/assets/metronic_v3.3.0/theme/assets/admin/layout3/scripts/demo.js" type="text/javascript"></script>

<script>
    jQuery(document).ready(function() {
        // initiate layout and plugins
        Metronic.init(); // init metronic core components
        Layout.init(); // init current layout
        Demo.init(); // init demo features
    });
</script>
<!-- END JAVASCRIPTS -->

<!-- END BODY -->
</body>

</body>

</html>