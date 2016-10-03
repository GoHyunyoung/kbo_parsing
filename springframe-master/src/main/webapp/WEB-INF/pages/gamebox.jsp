<%--
  Created by IntelliJ IDEA.
  User: moonlight
  Date: 2016. 9. 1.
  Time: 오후 9:24
  To change this template use File | Settings | File Templates.
--%>

<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<html>
<head>
    <link href="/resources/assets/css/index.css" rel="stylesheet" type="text/css">
</head>
<body>
<c:forEach var="article" items="${articleArrayList}">
<div class="portlet-body">
    <div class="row number-stats margin-bottom-30">
        <div class="col-md-2">
            <div class="stat-left">
                <div class="stat-number">
                    <div class="title">Away</div>
                    <div class="number">${article.head.substring(0,3)}</div>
                </div>
            </div>
        </div>
        <div class="emblem-left col-md-2">
            <a><img src="/resources/images/emblem_image/emblemB_${article.awayT}.png" alt="${article.awayT}"></a>
        </div>
        <div class="scorepoint col-md-4">
            <span>${article.head.substring(3,5)} </span> <span>: </span>
            <span>${article.head.substring(article.head.length() -2)}</span>
        </div>
        <div class="emblem-right col-md-2">
            <a><img src="/resources/images/emblem_image/emblemB_${article.homeT}.png" alt="${article.homeT}"></a>
        </div>
        <div class="col-md-2">
            <div class="stat-right">
                <div class="stat-number">
                    <div class="title">Home</div>
                    <div class="number">${article.head.substring(article.head.length() -5,article.head.length() -2)}</div>
                </div>
            </div>
        </div>
    </div>
    <div class="table-scrollable table-scrollable-borderless">
        <table class="table table-hover table-light">
            <thead>
            <tr class="uppercase">
                <th>TEAM</th>
                <div class="width35">
                    <th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th>
                    <th>8</th><th>9</th><th>10</th><th>11</th><th>12</th><th>R</th><th>H</th><th>E</th><th>B</th>
                </div>
            </tr>
            </thead>
            <tbody>
            <tr class="awayBox">
                <td class="bold-center">${article.head.substring(0,3)}</td>
                <div class="width35">
                    <td>${article.a1}</td>
                    <td>${article.a2}</td>
                    <td>${article.a3}</td>
                    <td>${article.a4}</td>
                    <td>${article.a5}</td>
                    <td>${article.a6}</td>
                    <td>${article.a7}</td>
                    <td>${article.a8}</td>
                    <td>${article.a9}</td>
                    <td>${article.a10}</td>
                    <td>${article.a11}</td>
                    <td>${article.a12}</td>
                    <td>${article.AR}</td>
                    <td>${article.AH}</td>
                    <td>${article.AE}</td>
                    <td>${article.AB}</td>
                </div>
            </tr>
            <tr class="homeBox">
                <td class="bold-center">${article.head.substring(article.head.length() -5,article.head.length() -2)}</td>
                <div class="width35">
                    <td>${article.h1}</td>
                    <td>${article.h2}</td>
                    <td>${article.h3}</td>
                    <td>${article.h4}</td>
                    <td>${article.h5}</td>
                    <td>${article.h6}</td>
                    <td>${article.h7}</td>
                    <td>${article.h8}</td>
                    <td>${article.h9}</td>
                    <td>${article.h10}</td>
                    <td>${article.h11}</td>
                    <td>${article.h12}</td>
                    <td>${article.HR}</td>
                    <td>${article.HH}</td>
                    <td>${article.HE}</td>
                    <td>${article.HB}</td>
                </div>
            </tr>
            </tbody>
        </table><br/>
        <c:forEach var="wlPitcher" items="${WinlosePitcherArrayList}">
        <div class="pitcher-box col-md-12">
            <br/>
            <ul class="list_result">
                <li class="col-md-2"></li>
                <c:choose>
                    <c:when test="${article.emblem == article.awayT}">
                        <li class="col-md-4">
                            <span class="thumb_vs">
                                <a class="thumb_round thumb_round120">
                                    <img src="${wlPitcher.winPlayerFaceUrl}" width="120" height="150" class="thumb_g" onerror="this.src=namespace('SPORTS_GAMECENTER.CONFIG').PLAYER_NOIMAGE">
                                    <span class="frame_round"></span>
                                </a>
                                <span class="mark_tip mark_blue"><span class="txt_gc">승</span></span>
                            </span>
                            <dl class="info_result">
                                <dt class="tit_name">${wlPitcher.winPlayerName}</dt>
                                <dd class="desc_result">
                                    시즌 ${wlPitcher.winPlayerWinCount}승 ${wlPitcher.winPlayerLoseCount}패 / ERA ${wlPitcher.winPlayerERA}
                                </dd>
                            </dl>
                        </li>
                        <li class="col-md-4">
                            <span class="thumb_vs">
                                <a class="thumb_round thumb_round120">
                                    <img src="${wlPitcher.losePlayerFaceUrl}" width="120" height="150" class="thumb_g" onerror="this.src=namespace('SPORTS_GAMECENTER.CONFIG').PLAYER_NOIMAGE">
                                    <span class="frame_round"></span>
                                </a>
                                <span class="mark_tip mark_gray"><span class="txt_gc">패</span></span>
                            </span>
                            <dl class="info_result">
                                <dt class="tit_name">${wlPitcher.losePlayerName}</dt>
                                <dd class="desc_result">
                                    시즌 ${wlPitcher.losePlayerWinCount}승 ${wlPitcher.losePlayerLoseCount}패 / ERA ${wlPitcher.losePlayerERA}
                                </dd>
                                <br/>
                            </dl>
                        </li>
                    </c:when>
                    <c:otherwise>
                        <li class="col-md-4">
                            <span class="thumb_vs">
                                <a class="thumb_round thumb_round120">
                                    <img src="${wlPitcher.losePlayerFaceUrl}" width="120" height="150" class="thumb_g" onerror="this.src=namespace('SPORTS_GAMECENTER.CONFIG').PLAYER_NOIMAGE">
                                    <span class="frame_round"></span>
                                </a>
                                <span class="mark_tip mark_gray"><span class="txt_gc">패</span></span>
                            </span>
                            <dl class="info_result">
                                <dt class="tit_name">${wlPitcher.losePlayerName}</dt>
                                <dd class="desc_result">
                                    시즌 ${wlPitcher.losePlayerWinCount}승 ${wlPitcher.losePlayerLoseCount}패 / ERA ${wlPitcher.losePlayerERA}
                                </dd>
                            </dl>
                        </li>
                        <li class="col-md-4">
                            <span class="thumb_vs">
                                <a class="thumb_round thumb_round120">
                                    <img src="${wlPitcher.winPlayerFaceUrl}" width="120" height="150" class="thumb_g" onerror="this.src=namespace('SPORTS_GAMECENTER.CONFIG').PLAYER_NOIMAGE">
                                    <span class="frame_round"></span>
                                </a>
                                <span class="mark_tip mark_blue"><span class="txt_gc">승</span></span>
                            </span>
                            <dl class="info_result">
                                <dt class="tit_name">${wlPitcher.winPlayerName}</dt>
                                <dd class="desc_result">
                                    시즌 ${wlPitcher.winPlayerWinCount}승 ${wlPitcher.winPlayerLoseCount}패 / ERA ${wlPitcher.winPlayerERA}
                                </dd>
                                <br/>
                            </dl>
                        </li>
                    </c:otherwise>
                </c:choose>

                <li class="col-md-2"></li>
            </ul>
        </div>
        </c:forEach>

        <ul class="list_graph col-md-12">
            <li class="fst">
                <span class="txt_gc tit_hit">안타</span>
                <span class="vs_graph vs_team1">
                    <span class="rod_graph" data-name="${article.awayT}" style="width:${article.AH*4+6}%">
                        <span class="num_g">${article.AH}</span>
                    </span>
                </span>
                <span class="screen_out"> vs</span>
                <span class="vs_graph vs_team2">
                    <span class="rod_graph2" data-name="${article.homeT}" style="width:${article.HH*4+6}%">
                        <span class="num_g">${article.HH}</span>
                    </span>
                </span>
            </li>
            <li>
                <span class="txt_gc tit_homerun">홈런</span>
                <span class="vs_graph vs_team1">
                    <span class="rod_graph" data-name="${article.awayT}" style="width:${article.awayHR*8+6}%">
                        <span class="num_g">${article.awayHR}</span>
                    </span>
                </span>
                <span class="screen_out"> vs</span>
                <span class="vs_graph vs_team2">
                    <span class="rod_graph2" data-name="${article.homeT}" style="width:${article.homeHR*8+6}%">
                        <span class="num_g">${article.homeHR}</span>
                    </span>
                </span>
            </li>
            <li>
                <span class="txt_gc tit_strikeout2">탈삼진</span>
                <span class="vs_graph vs_team1">
                    <span class="rod_graph" data-name="${article.awayT}" style="width:${article.awaySO*5+6}%">
                        <span class="num_g">${article.awaySO}</span>
                    </span>
                </span>
                <span class="screen_out"> vs</span>
                <span class="vs_graph vs_team2">
                    <span class="rod_graph2" data-name="${article.homeT}" style="width:${article.homeSO*5+6}%">
                        <span class="num_g">${article.homeSO}</span>
                    </span>
                </span>
            </li>
            <li>
                <span class="txt_gc tit_sab">도루</span>
                <span class="vs_graph vs_team1">
                    <span class="rod_graph" data-name="${article.awayT}" style="width:${article.awaySB*8+6}%">
                        <span class="num_g">${article.awaySB}</span>
                    </span>
                </span>
                <span class="screen_out"> vs</span>
                <span class="vs_graph vs_team2">
                    <span class="rod_graph2" data-name="${article.homeT}" style="width:${article.homeSB*8+6}%">
                        <span class="num_g">${article.homeSB}</span>
                    </span>
                </span>
            </li>
            <li>
                <span class="txt_gc tit_mistake">실책</span>
                <span class="vs_graph vs_team1">
                    <span class="rod_graph" data-name="${article.awayT}" style="width:${article.AE*8+6}%">
                        <span class="num_g">${article.AE}</span>
                    </span>
                </span>
                <span class="screen_out"> vs</span>
                <span class="vs_graph vs_team2">
                    <span class="rod_graph2" data-name="${article.homeT}" style="width:${article.HE*8+6}%">
                        <span class="num_g">${article.HE}</span>
                    </span>
                </span>
            </li>
            <li>
                <span class="txt_gc tit_dp">병살</span>
                <span class="vs_graph vs_team1">
                    <span class="rod_graph" data-name="${article.awayT}" style="width:${article.awayGDP*8+6}%">
                        <span class="num_g">${article.awayGDP}</span>
                    </span>
                </span>
                <span class="screen_out"> vs</span>
                <span class="vs_graph vs_team2">
                    <span class="rod_graph2" data-name="${article.homeT}" style="width:${article.homeGDP*8+6}%">
                        <span class="num_g">${article.homeGDP}</span>
                    </span>
                </span>
            </li>
            <li>
                <span class="txt_gc tit_lob">잔루</span>
                <span class="vs_graph vs_team1">
                    <span class="rod_graph" data-name="${article.awayT}" style="width:${article.awayLOB*4+6}%">
                        <span class="num_g">${article.awayLOB}</span>
                    </span>
                </span>
                <span class="screen_out"> vs</span>
                <span class="vs_graph vs_team2">
                    <span class="rod_graph2" data-name="${article.homeT}" style="width:${article.homeLOB*4+6}%">
                        <span class="num_g">${article.homeLOB}</span>
                    </span>
                </span>
            </li>
            <li>
                <span class="txt_gc tit_walk">사사구</span>
                <span class="vs_graph vs_team1">
                    <span class="rod_graph" data-name="${article.awayT}" style="width:${article.AB*5+6}%">
                        <span class="num_g">${article.AB}</span>
                    </span>
                </span>
                <span class="screen_out"> vs</span>
                <span class="vs_graph vs_team2">
                    <span class="rod_graph2" data-name="${article.homeT}" style="width:${article.HB*5+6}%">
                        <span class="num_g">${article.HB}</span>
                    </span>
                </span>
            </li>
        </ul>
    </div>
</div>
</c:forEach>
</body>
</html>