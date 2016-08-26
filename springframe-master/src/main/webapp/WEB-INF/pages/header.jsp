<%--
  Created by IntelliJ IDEA.
  User: owner
  Date: 2016-08-13
  Time: 오후 6:05
  To change this template use File | Settings | File Templates.
--%>

<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <script type="text/javascript" src="../../resources/assets/javascript/searchResult.js"></script>
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
            <form class="search-form" action="search.jsp" method="GET">
                <div class="col-md-3">
                    <c:choose>
                        <c:when test="${articleList[0]==null}">
                            <input class="form-control form-control-inline date-picker" size="16" type="text"
                                   placeholder="Search from Date" value="">
                        </c:when>
                        <c:otherwise>
                            <input class="form-control form-control-inline date-picker" size="16" type="text"
                                   placeholder="${articleList[0].date.substring(0,4)}-
                                   ${articleList[0].date.substring(4,6)}-
                                   ${articleList[0].date.substring(6,articleList[0].date.length())}" value="">
                        </c:otherwise>
                    </c:choose>
                </div>
            </form>

            <!-- END HEADER SEARCH BOX -->
            <!-- BEGIN MEGA MENU -->
            <div class="hor-menu">
                <ul class="nav navbar-nav">
                    <li>
                        <a href="/index">Mr.Writer?</a>
                    </li>
                    <li>
                        <a href="/timeline">Timeline</a>
                    </li>
                    <li>
                        <a href="/boxscore">BoxScore</a>
                    </li>
                    <li>
                        <a href="/">Etc</a>
                    </li>
                </ul>
            </div>
            <!-- END MEGA MENU -->
        </div>
    </div>
    <!-- END HEADER MENU -->
</div>
<!-- END HEADER -->
</body>
</html>
