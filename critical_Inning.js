this["JST_PRECOMPILE"] = this["JST_PRECOMPILE"] || {};

this["JST_PRECOMPILE"]["adCard"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape;
	with (obj) {
		__p += '<div id="ad-card">\n\t<script>\n\t\t$(function(){\n\t\t\t$.getScript("http://display.ad.daum.net/imp?slotid=' +
		((__t = ( SLOT_ID )) == null ? '' : __t) +
		'");\n\t\t});\t\n\t</script>\n</div>\n';

	}
	return __p
};

this["JST_PRECOMPILE"]["adSponsor"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape;
	with (obj) {
		__p += '<script>\n\t$(function(){\n\t\t$.getScript("http://display.ad.daum.net/imp?slotid=' +
		((__t = ( SLOT_ID )) == null ? '' : __t) +
		'");\n\t});\t\n</script>';

	}
	return __p
};

this["JST_PRECOMPILE"]["comment"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape;
	with (obj) {
		__p += '<div class="cmtlayer_head">\n\t<strong class="tit_layer">영상 댓글</strong>\n</div>\n<div class="cmtlayer_body">\n\t<strong class="tit_talk">에디터 Talk!</strong>\n\t<p class="desc_talk">“ 위기의 한화를 김태균이 살립니다.주장의 홈런으로 한화가 추격의 불씨를 당깁니다. 야구 재밌어요~~ ”</p>\n\t<div class="comment_template_content" id="alexCommentWrapper"></div>\n</div>\n<div class="cmtlayer_foot">\n\t<a href="#none" class="link_close"><span class="img_highlight">닫기</span></a>\n</div>\n';

	}
	return __p
};

this["JST_PRECOMPILE"]["commentCount"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape;
	with (obj) {
		__p += '<span class="img_highlight">댓글</span>' +
		((__t = (COUNT)) == null ? '' : __t);

	}
	return __p
};

this["JST_PRECOMPILE"]["cover"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape;
	with (obj) {
		__p += '<div class="template_comm cover">\n\t<div class="title">\n\t\t<h2>\n\t\t\t<span class="match_name">\n\t\t\t\t<span class="team_name team_name1">\n\t\t\t\t\t<img src="' +
		((__t = (AWAY_TEAM_LOGO)) == null ? '' : __t) +
		'" class="img_logo" alt="">\n\t\t\t\t\t' +
		((__t = (AWAY_TEAM_NAME)) == null ? '' : __t) +
		'\n\t\t\t\t</span>\n\t\t\t\t<span class="img_highlight">vs</span>\n\t\t\t\t<span class="team_name team_name2">\n\t\t\t\t\t<img src="' +
		((__t = (HOME_TEAM_LOGO)) == null ? '' : __t) +
		'" class="img_logo" alt="">\n\t\t\t\t\t' +
		((__t = (HOME_TEAM_NAME)) == null ? '' : __t) +
		'\n\t\t\t\t</span>\n\t\t\t</span>\n\t\t\t<span class="match_sequence">' +
		((__t = ( MATCH_SEQ )) == null ? '' : __t) +
		'차전</span>\n\t\t</h2>\n\t\t<p class="info">\n\t\t\t<span class="location">' +
		((__t = ( BALLPARK_NAME )) == null ? '' : __t) +
		'</span>\n\t\t\t<span class="date">' +
		((__t = ( YEAR )) == null ? '' : __t) +
		'.' +
		((__t = ( MONTH )) == null ? '' : __t) +
		'.' +
		((__t = ( DAY )) == null ? '' : __t) +
		' ' +
		((__t = ( TIME )) == null ? '' : __t) +
		'</span>\n\t\t</p>\n\t\t<a href="#none" id="ad-sponsor" class="link_ad"></a>\n\t\t<div class="img_highlight bg_scroll">스크롤 보기</div>\n\t\t<div class="background_content cover_bg show">\n\t\t\t<div class="bg_cover" style="background-image:url(' +
		((__t = (BACKGROUND_IMAGE)) == null ? '' : __t) +
		')"></div>\n\t\t</div>\n\t</div>\n\t<div class="ico_arrow rw_hide">\n\t\t<img src="http://i1.daumcdn.net/img-section/3min/arrow.png" width="10" height="19" />\n\t</div>\n</div>\n';

	}
	return __p
};

this["JST_PRECOMPILE"]["divider"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
	function print() { __p += __j.call(arguments, '') }
	with (obj) {


		var titles = TITLE.split("<br>");
		;
		__p += '\n<div class="template_comm divider">\n\t<div class="wrap">\n\t\t<h3>' +
		((__t = ( INNING_STRING )) == null ? '' : __t) +
		'</h3>\n\t\t<p>\n\t\t\t<span class="txt_g">\n\t\t\t\t<span class="txt_g2">' +
		((__t = ( titles[0] )) == null ? '' : __t) +
		'</span>\n\t\t\t</span>\n\t\t\t';

		if(titles.length > 1){
			;
			__p += '\n\t\t\t\t<br>\n\t\t\t\t<span class="txt_g">\n\t\t\t\t\t<span class="txt_g2">' +
			((__t = ( titles[1] )) == null ? '' : __t) +
			'</span>\n\t\t\t\t</span>\n\t\t\t';

		}
		;
		__p += '\n\t\t</p>\n\n\t\t';

		if(!(_.isEmpty(SITUATION))){
			;
			__p += '\n\t\t\t<dl class="list_info">\n\t\t\t\t<dt>상황</dt>\n\t\t\t\t<dd>' +
			((__t = ( SITUATION)) == null ? '' : __t) +
			'</dd>\n\t\t\t</dl>\n\t\t';

		}
		;
		__p += '\n\t\t\t<dl class="list_info list_info2">\n\t\t';

		if(!(_.isEmpty(PITCHER))){
			;
			__p += '\n\t\t\t<dt>투수</dt>\n\t\t\t<dd>' +
			((__t = ( PITCHER)) == null ? '' : __t) +
			'</dd>\n\t\t';

		}

		if(!(_.isEmpty(BATTER))){
			;
			__p += '\n\t\t\t<dt>타자</dt>\n\t\t\t<dd>' +
			((__t = ( BATTER)) == null ? '' : __t) +
			'</dd>\n\t\t';

		}
		;
		__p += '\n\t\t\t</dl>\n\t</div>\n\t<div class="background_content divider_bg" style="background-image: url(' +
		((__t = ( BACKGROUND_IMAGE )) == null ? '' : __t) +
		')">\n\t</div>\n</div>\n';

	}
	return __p
};

this["JST_PRECOMPILE"]["end"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
	function print() { __p += __j.call(arguments, '') }
	with (obj) {

		if (!HAS_RENDERED) { ;
			__p += '\n<div class="template_comm end">\n\t<div class="card_template_content">\n\t\t<div class="share_end">\n\t\t\t<div class="share">\n\t\t\t\t<a href="#none" class="link_cmt">\n\t\t\t\t\t<em class="emph_g">0</em>개 댓글 전체보기<span class="img_highlight"></span>\n\t\t\t\t</a>\n\t\t\t\t<button>App Share</button>\n\t\t\t\t<ul class="non_app_share">\n\t\t\t\t\t<li class="kakaostory"><a href="#">카카오스토리 공유하기</a></li>\n\t\t\t\t\t<li class="twitter"><a href="#">트위터 공유하기</a></li>\n\t\t\t\t\t<li class="facebook"><a href="#">페이스북 공유하기</a></li>\n\t\t\t\t</ul>\n\t\t\t</div>\n\t\t</div>\n\n\t\t<div class="game_center">\n';
		} ;
		__p += '\n\n';
		if (GAMES_OF_GAME_DATE && GAMES_OF_GAME_DATE.length) { ;
			__p += '\n\t\t\t<h3>\n\t\t\t\t' +
			((__t = ( GAME_DATE.getMonth() + 1 )) == null ? '' : __t) +
			'월 ' +
			((__t = ( GAME_DATE.getDate() )) == null ? '' : __t) +
			'일 다른경기\n\t\t\t</h3>\n\t\t\t<ul>\n\n\t\t\t';
			
			for (var i = 0, length = GAMES_OF_GAME_DATE.length; i<length; i++) { 
				var GAME = GAMES_OF_GAME_DATE[i],
				NAME = GAME['name'].split(' '), 
				SEQUENCE = NAME.splice(3, 1)[0],
				NAME = NAME.join(' ');
				;
				__p += '\n\t\t\t\t<li><a href="./' +
				((__t = ( GAME.gameId )) == null ? '' : __t) +
				'">\n\t\t\t\t\t<span class="photo" style="background-image:url(\'';
				print(GAME.thumbnail || 'thumbnail?') ;
				__p += '\')"></span>\n\t\t\t\t\t' +
				((__t = ( NAME )) == null ? '' : __t) +
				' <span class="sequence">' +
				((__t = ( SEQUENCE )) == null ? '' : __t) +
				'</span>\n\t\t\t\t</a></li>\n\t\t\t';
			} ;
			__p += '\n\n\t\t\t</ul>\n';
		} ;
		__p += '\n\t\t\t<p class="game_center_link">\n\t\t\t\t<a href="http://m.sports.media.daum.net/m/sports/" class="mobile" target="_blank">Daum 스포츠 모바일</a>\n\t\t\t\t<a href="http://sports.media.daum.net/sports/" class="pc" target="_blank">Daum 스포츠</a>\n\t\t\t</p>\n';
		if (!HAS_RENDERED) { ;
			__p += '\n\t\t</div>\n\t</div>\n</div>\n';
		} ;


	}
	return __p
};

this["JST_PRECOMPILE"]["games"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
	function print() { __p += __j.call(arguments, '') }
	with (obj) {


		var league = (GAME_CATEGORY || "").toUpperCase();
		;
		__p += '\n<div class="games_wrap">\n<header>\n\t<p class="gamecenter_link">\n\t\t<button>Daum ' +
		((__t = (league)) == null ? '' : __t) +
		'게임센터</button>\n\t</p>\n\t<p class="close">\n\t\t<button>뒤로</button>\n\t</p>\n\t<h1><span>경기목록</span></h1>\n\t<p class="date">\n\t\t<button class="previous">이전달</button>\n\t\t<span class="current">\n\t\t\t';
		print(SEASON_MONTH.substr(0, 4) + '.' + SEASON_MONTH.substr(4, 2)) ;
		__p += '\n\t\t</span>\n\t\t<button class="next">다음달</button>\n\t</p>\n\t<ul class="tabs">\n\t\t<li id="games-recent" class="';
		print(SORT_METHOD === 'recent' ? 'on' : '') ;
		__p += '"><button>최신순</button></li>\n\t\t<li id="games-team">\n\t\t\t<button class="';
		print(SELECTED_TEAM ? 'on' : '') ;
		__p += '">';
		print(SELECTED_TEAM || '전체') ;
		__p += '</button>\n\t\t\t';

		if(league == "KBO") {
			;
			__p += '\n\t\t\t\t\t<ul class="team-filter">\n\t\t\t\t\t\t\t<li><button class="team_all ';
			print(SELECTED_TEAM ? '' : 'on') ;
			__p += '" data-id="전체">전체</button></li>\n\t\t\t\t\t';

			for (var i = 0, length = TEAM_INFO.length; i < TEAM_INFO.length; i++) {
				;
				__p += '\n\t\t\t\t\t\t\t<li><button class="team_logo ';
				print(SELECTED_TEAM == TEAM_INFO[i]['teamName'] ? 'on' : '') ;
				__p += '" data-id="' +
				((__t = (TEAM_INFO[i]['teamId'])) == null ? '' : __t) +
				'" style="background-image: url(' +
				((__t = ( TEAM_LOGO[i] )) == null ? '' : __t) +
				')">' +
				((__t = ( TEAM_INFO[i]['teamName'] )) == null ? '' : __t) +
				'</button></li>\n\t\t\t\t\t';

			}
			;
			__p += '\n\t\t\t\t\t</ul>\n\t\t\t';

		}
		;
		__p += '\n\t\t</li>\n\t</ul>\n</header>\n<div class="list">\n\t';


		for (var i = 0; i < GAME_LIST.length; i++) {

			var length = GAME_LIST.length, GAME = GAME_LIST[i], DATE = GAME.date, PREVIOUS_DATE;
			;
			__p += '\n\t\t<section class="day">\n\t\t\t';
			if (PREVIOUS_DATE != GAME.date && SORT_METHOD === 'recent') { ;
				__p += '\n\t\t\t<h1>\n\t\t\t\t';

				print(Number(DATE.substr(4, 2)) + '월 ' + Number(DATE.substr(6, 2)) + '일');
				PREVIOUS_DATE = DATE;
				;
				__p += '\n\t\t\t</h1>\n\t\t\t';
			} ;
			__p += '\n\t\t\t<section class="game">\n\t\t\t\t<a href="';

			var pathnames = location.pathname.split('/');

			pathnames[pathnames.length - 1] = GAME.gameId;
			print(pathnames.join('/'));
			;
			__p += '">\n\t\t\t\t\t<h2>\n\t\t\t\t\t\t';
			print(GAME.name.replace(SELECTED_TEAM, '<em>' + SELECTED_TEAM + '</em>') || 'name?') ;
			__p += '\n\t\t\t\t\t\t';
			if (SORT_METHOD !== 'recent') { ;
				__p += '\n\t\t\t\t\t\t<span class="date">' +
				((__t = ( Number(DATE.substr(4, 2)) + '월 ' + Number(DATE.substr(6, 2)) + '일' )) == null ? '' : __t) +
				'</span>\n\t\t\t\t\t\t';
			} ;
			__p += '\n\t\t\t\t\t</h2>\n\t\t\t\t\t<p class="link_cmt"><span class="img_highlight">댓글</span>' +
			((__t = (GAME.commentCount)) == null ? '' : __t) +
			'</p>\n\t\t\t\t\t<p class="photo" style="background-image: url(\'';
			print(GAME.thumbnail || 'thumbnail?') ;
			__p += '\')">\n\t\t\t\t\t\t<span class="title">';
			print(GAME.title.replace(SELECTED_TEAM, '<em>' + SELECTED_TEAM + '</em>') || 'title?') ;
			__p += '</span>\n\t\t\t\t\t</p>\n\t\t\t\t</a>\n\t\t\t</section>\n\t\t</section>\n\t';

		}
		;
		__p += '\n\t';

		if (!GAME_LIST.length) {
			;
			__p += '\n\t\t\t<p><div class="no_game" style="text-align:center;">\n\t\t\t\t';

			var month = SEASON_MONTH.substr(4, 2),
			previousMonth;

			if (month.substr(0, 1) === '0') {
				month = month.substr(1, 1);
			}

			previousMonth = Number(month) - 1;
			if (!previousMonth) {
				previousMonth = 12;
			}
			print(month);
			;
			__p += '월 경기가 아직 없습니다.<br>\n\t\t\t\t<button>' +
			((__t = ( previousMonth )) == null ? '' : __t) +
			'월 경기보기</button>\n\t\t\t<div></p>\n\t';

		}
		;
		__p += '\n\t<p class="more">\n\t\t<button>더보기</button>\n\t</p>\n</div>\n</div>';

	}
	return __p
};

this["JST_PRECOMPILE"]["lineup"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
	function print() { __p += __j.call(arguments, '') }
	with (obj) {
		__p += '<div class="template_comm lineup">\n\t<div class="card_template_content">\n\t\t';

		if(!(_.isEmpty(VIEWPOINT))){
			;
			__p += '\n\t\t\t<h3 class="card tit_hpoint">타자 관전 포인트</h3>\n\t\t\t<p class="desc_point">"' +
			((__t = (VIEWPOINT)) == null ? '' : __t) +
			'"</p>\n\t\t';

		}
		;
		__p += '\n\t\t<h3 class="card">선발 라인업</h3>\n\t\t<span class="txt_key">키플레이어</span>\n\t\t<div class="wrap">\n\t\t\t<table>\n\t\t\t\t<colgroup>\n\t\t\t\t\t<col class="position">\n\t\t\t\t\t<col class="name">\n\t\t\t\t\t<col class="batting_average">\n\t\t\t\t</colgroup>\n\t\t\t\t<col class="sequence">\n\t\t\t\t<colgroup>\n\t\t\t\t\t<col class="position">\n\t\t\t\t\t<col class="name">\n\t\t\t\t\t<col class="batting_average">\n\t\t\t\t</colgroup>\n\t\t\t\t<thead>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<th colspan="3">\n\t\t\t\t\t\t\t<div class="away">\n\t\t\t\t\t\t\t<span class="team_logo" style="background-image: url(' +
		((__t = ( AWAY_TEAM_LOGO )) == null ? '' : __t) +
		')"></span>\n\t\t\t\t\t\t\t' +
		((__t = ( LINEUP_AWAY_TEAM )) == null ? '' : __t) +
		'\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</th>\n\t\t\t\t\t\t<th>타순</th>\n\t\t\t\t\t\t<th colspan="3">\n\t\t\t\t\t\t\t<div class="home">\n\t\t\t\t\t\t\t<span class="team_logo" style="background-image: url(' +
		((__t = ( HOME_TEAM_LOGO )) == null ? '' : __t) +
		')"></span>\n\t\t\t\t\t\t\t' +
		((__t = ( LINEUP_HOME_TEAM )) == null ? '' : __t) +
		'\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</th>\n\t\t\t\t\t</tr>\n\t\t\t\t</thead>\n\t\t\t\t<tbody>\n\t\t\t\t\t';
		for(var i = 0, cnt = LINEUP_TABLE.length; i < cnt; i++) { ;
			__p += '\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td class="position away' +
			((__t = (
				LINEUP_TABLE[i].away.isKeyPlayer ? ' key-player' : ''
				)) == null ? '' : __t) +
			'"><span>' +
			((__t = ( LINEUP_TABLE[i].away.position )) == null ? '' : __t) +
			'</span></td>\n\t\t\t\t\t\t<td>' +
			((__t = ( LINEUP_TABLE[i].away.name )) == null ? '' : __t) +
			'</td>\n\t\t\t\t\t\t<td class="batting_average">\n\t\t\t\t\t\t\t' +
			((__t = ( LINEUP_TABLE[i].away.average )) == null ? '' : __t) +
			'\n\t\t\t\t\t\t\t' +
			((__t = ( LINEUP_TABLE[i].away.isKeyPlayer ? '<span class="key_player_mark">키플레이어</span>' : '' )) == null ? '' : __t) +
			'\n\t\t\t\t\t\t</td>\n\t\t\t\t\t\t<th>' +
			((__t = ( i + 1 )) == null ? '' : __t) +
			'</th>\n\t\t\t\t\t\t<td class="position home' +
			((__t = (
				LINEUP_TABLE[i].home.isKeyPlayer ? ' key-player' : ''
				)) == null ? '' : __t) +
			'"><span>' +
			((__t = ( LINEUP_TABLE[i].home.position )) == null ? '' : __t) +
			'</span></td>\n\t\t\t\t\t\t<td>' +
			((__t = ( LINEUP_TABLE[i].home.name )) == null ? '' : __t) +
			'</td>\n\t\t\t\t\t\t<td class="batting_average">\n\t\t\t\t\t\t\t' +
			((__t = ( LINEUP_TABLE[i].home.average )) == null ? '' : __t) +
			'\n\t\t\t\t\t\t\t' +
			((__t = ( LINEUP_TABLE[i].home.isKeyPlayer ? '<span class="key_player_mark">키플레이어</span>' : '' )) == null ? '' : __t) +
			'\n\t\t\t\t\t\t</td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t';
		} ;
		__p += '\n\t\t\t\t</tbody>\n\t\t\t</table>\n\t\t</div>\n\t</div>\n</div>\n';

	}
	return __p
};

this["JST_PRECOMPILE"]["navigator"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
	function print() { __p += __j.call(arguments, '') }
	with (obj) {
		__p += '<div class="navigator_wrap">\n<p class="close"><button>닫기</button></p>\n\t<ul>\n\t\t';
		for(var i = 0, cnt = NAV_SCENE.length; i < cnt; i++) { ;
			__p += '\n\t\t<li class="purpose-' +
			((__t = ( NAV_SCENE[i].purpose )) == null ? '' : __t) +
			'"';

			if (NAV_SCENE[i].background !== null) {
				;
				__p += ' style="background-image: url(' +
				((__t = ( NAV_SCENE[i].background )) == null ? '' : __t) +
				')"';

			}
			;
			__p += '>\n\t\t\t<button data-content-id="' +
			((__t = ( NAV_SCENE[i].contentsId )) == null ? '' : __t) +
			'">\n\t\t\t\t';

			if(_.isEqual(NAV_SCENE[i].purpose,"divider") && NAV_SCENE[i].data.info && _.isEqual(NAV_SCENE[i].data.info.eventType,"critical")){
				;
				__p += '\n\t\t\t\t\t<strong class="img_highlight ico_decisive">승부처</strong>\n\t\t\t\t';

			}
			;
			__p += '\n\t\t\t\t<span class="label">' +
			((__t = ( NAV_SCENE[i].label )) == null ? '' : __t) +
			'</span>\n\t\t\t\t';
			if (NAV_SCENE[i].footer !== null) { ;
				__p += '\n\t\t\t\t<span class="footer">' +
				((__t = ( NAV_SCENE[i].footer )) == null ? '' : __t) +
				'</span>\n\t\t\t\t';
			} ;
			__p += '\n\t\t\t</button>\n\t\t</li>\n\t\t';
		} ;
		__p += '\n\t\t<li class="game-center">\n\t\t\t<a href="http://m.sports.media.daum.net/m/sports/gamecenter/' +
		((__t = ( GAME_ID )) == null ? '' : __t) +
		'/cast">\n\t\t\t\t<span class="label">게임센터<br>바로가기</span>\n\t\t\t\t<span class="footer">Daum 스포츠</span>\n\t\t\t</a>\n\t\t</li>\n\t</ul>\n</div>';

	}
	return __p
};

this["JST_PRECOMPILE"]["news"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
	function print() { __p += __j.call(arguments, '') }
	with (obj) {
		__p += '<div class="template_comm news">\n\t<div class="news_wrapper">\n\t\t<h3>' +
		((__t = ( SUBJECT )) == null ? '' : __t) +
		'</h3>\n\t\t<p class="info">\n\t\t\t<span class="source">' +
		((__t = ( SOURCE )) == null ? '' : __t) +
		'</span>\n\t\t\t<span class="date">' +
		((__t = ( DATE )) == null ? '' : __t) +
		'</span>\n\t\t</p>\n\t\t<div class="photo"></div>\n\t\t<div class="body"></div>\n\t</div>\n\t<div class="supplement">\n\t\t<span class="share">\n\t\t\t<button>공유</button>\n\t\t\t<ul class="non_app_share">\n\t\t\t\t<li class="kakaostory"><a href="#">카카오스토리 공유하기</a></li>\n\t\t\t\t<li class="twitter"><a href="#">트위터 공유하기</a></li>\n\t\t\t\t<li class="facebook"><a href="#">페이스북 공유하기</a></li>\n\t\t\t</ul>\n\t\t</span>\n\t\t';
		if (PLAYER_NAME !== '') { ;
			__p += '\n\t\t<span class="player">\n\t\t\t<button class="' +
			((__t = ( PLAYER_TEAM_ID )) == null ? '' : __t) +
			'">' +
			((__t = ( PLAYER_NAME )) == null ? '' : __t) +
			'</button>\n\t\t</span>\n\t\t';
		} ;
		__p += '\n\t</div>\n</div>\n';

	}
	return __p
};

this["JST_PRECOMPILE"]["newsreader"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape;
	with (obj) {
		__p += '<p class="close"><button>닫기</button></p>\n<h3>' +
		((__t = ( SUBJECT )) == null ? '' : __t) +
		'</h3>\n<div class="body">' +
		((__t = ( ARTICLE )) == null ? '' : __t) +
		'</div>\n';

	}
	return __p
};

this["JST_PRECOMPILE"]["photo"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
	function print() { __p += __j.call(arguments, '') }
	with (obj) {
		__p += '<div class="template_comm photo">\n\t<div class="photo"></div>\n\t<div class="photo-extra">\n\t\t<img src="' +
		((__t = ( PHOTO )) == null ? '' : __t) +
		'" alt="">\n\t\t<h3>' +
		((__t = ( TITLE )) == null ? '' : __t) +
		'</h3>\n\t</div>\n\t<div class="supplement">\n\t\t<span class="share">\n\t\t\t<button>공유</button>\n\t\t\t<ul class="non_app_share">\n\t\t\t\t<li class="kakaostory"><a href="#">카카오스토리 공유하기</a></li>\n\t\t\t\t<li class="twitter"><a href="#">트위터 공유하기</a></li>\n\t\t\t\t<li class="facebook"><a href="#">페이스북 공유하기</a></li>\n\t\t\t</ul>\n\t\t</span>\n\t\t';
		if (PLAYER_NAME !== '') { ;
			__p += '\n\t\t<span class="player">\n\t\t\t<button class="' +
			((__t = ( PLAYER_TEAM_ID )) == null ? '' : __t) +
			'">' +
			((__t = ( PLAYER_NAME )) == null ? '' : __t) +
			'</button>\n\t\t</span>\n\t\t';
		} ;
		__p += '\n\t</div>\n</div>\n';

	}
	return __p
};

this["JST_PRECOMPILE"]["pitcher"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
	function print() { __p += __j.call(arguments, '') }
	with (obj) {
		__p += '<div class="template_comm pitcher">\n\t\t';

		if(!(_.isEmpty(VIEWPOINT))){
			;
			__p += '\n\t\t\t<h3 class="card tit_ppoint">투수 관전 포인트</h3>\n\t\t\t<p class="desc_point">"' +
			((__t = (VIEWPOINT)) == null ? '' : __t) +
			'"</p>\n\t\t';

		}
		;
		__p += '\n\t\t<h3 class="card">선발 투수</h3>\n\t\t<dl class="player_pitcher">\n\t\t\t<div class="vs_rect"></div>\n\t\t\t<div class="pitcher_comm pitcher_away">\n\t\t\t\t<span class="photo"><img src="' +
		((__t = ( PITCHER_AWAY_IMAGE )) == null ? '' : __t) +
		'" alt=""></span>\n\t\t\t\t<strong class="name">' +
		((__t = ( PITCHER_AWAY_NAME )) == null ? '' : __t) +
		'</strong>\n\t\t\t\t<span class="info">' +
		((__t = ( PITCHER_AWAY_TEAM_NAME )) == null ? '' : __t) +
		' 선발투수</span>\n\t\t\t</div>\n\t\t\t<div class="pitcher_comm pitcher_home">\n\t\t\t\t<span class="photo"><img src="' +
		((__t = ( PITCHER_HOME_IMAGE )) == null ? '' : __t) +
		'" alt="" onerror="this.src=namespace(\'SPORTS_3MIN\').App.PLAYER_NOIMAGE"></span>\n\t\t\t\t<strong class="name">' +
		((__t = ( PITCHER_HOME_NAME )) == null ? '' : __t) +
		'</strong>\n\t\t\t\t<span class="info">' +
		((__t = ( PITCHER_HOME_TEAM_NAME )) == null ? '' : __t) +
		' 선발투수</span>\n\t\t\t</div>\n\t\t</dl>\n\t\t<div class="vs_graph">\n\t\t\t<div id="season_stat" class="on">\n\t\t\t\t<h4>시즌 전적<button class="tab" data-tab="season_stat">보기</button></h4>\n\t\t\t\t<ul class="list_record">\n\t\t\t\t\t' +
		((__t = ( SEASON_STAT_GRAPH )) == null ? '' : __t) +
		'\n\t\t\t\t</ul>\n\t\t\t\t<div class="underline"></div>\n\t\t\t</div>\n\t\t\t<div id="vs_stat">\n\t\t\t\t<h4>상대팀 전적<button class="tab" data-tab="vs_stat">보기</button>\t</h4>\n\t\t\t\t<ul class="list_record">\n\t\t\t\t\t' +
		((__t = ( VS_STAT_GRAPH )) == null ? '' : __t) +
		'\n\t\t\t\t</ul>\n\t\t\t</div>\n\t\t</div>\n</div>\n';

	}
	return __p
};

this["JST_PRECOMPILE"]["playercard"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
	function print() { __p += __j.call(arguments, '') }
	with (obj) {
		__p += '<div class="photo"><img src="' +
		((__t = ( THUMBNAIL )) == null ? '' : __t) +
		'" alt="' +
		((__t = ( NAME )) == null ? '' : __t) +
		'"></div>\n';
		if (TYPE == 'season_record') { ;
			__p += '\n<h2>시즌성적</h2>\n\t';
			if (IS_PITCHER) { ;
				__p += '\n<ul>\n\t<li><span class="label">평균 자책점</span> ' +
				((__t = ( ERA.toFixed(2) )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">승-패-세</span> ' +
				((__t = ( W )) == null ? '' : __t) +
				'-' +
				((__t = ( L )) == null ? '' : __t) +
				'-' +
				((__t = ( SV )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">피안타율</span> ' +
				((__t = ( HIT_RATIO.toFixed(3).replace('0.', '.') )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">WHIP</span> ' +
				((__t = ( WHIP.toFixed(2) )) == null ? '' : __t) +
				'</li>\n</ul>\n\t';
			} else { ;
				__p += '\n<ul>\n\t<li><span class="label">타율</span> ' +
				((__t = ( AVG.toFixed(3).replace('0.', '.') )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">타점</span> ' +
				((__t = ( RBI )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">홈런</span> ' +
				((__t = ( HR )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">볼넷</span> ' +
				((__t = ( BB )) == null ? '' : __t) +
				'</li>\n</ul>\n\t';
			} ;
			__p += '\n';
		} else if (TYPE == 'vsteam_record') { ;
			__p += '\n<h2>vs ' +
			((__t = ( OTHER_TEAM_NAME )) == null ? '' : __t) +
			'</h2>\n\t';
			if (IS_PITCHER) { ;
				__p += '\n<ul>\n\t<li><span class="label">이닝</span> ' +
				((__t = ( IP )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">평균 자책점</span> ' +
				((__t = ( ERA.toFixed(2) )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">승-패-세</span> ' +
				((__t = ( W )) == null ? '' : __t) +
				'-' +
				((__t = ( L )) == null ? '' : __t) +
				'-' +
				((__t = ( SV )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">피안타율</span> ' +
				((__t = ( HIT_RATIO.toFixed(3).replace('0.', '.') )) == null ? '' : __t) +
				'</li>\n</ul>\n\t';
			} else { ;
				__p += '\n<ul>\n\t<li><span class="label">타율</span> ' +
				((__t = ( AVG.toFixed(3).replace('0.', '.') )) == null ? '' : __t) +
				'<span class="sub"> (' +
				((__t = ( HIT )) == null ? '' : __t) +
				' /' +
				((__t = ( AB )) == null ? '' : __t) +
				')</span></li>\n\t<li><span class="label">타점</span> ' +
				((__t = ( RBI )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">홈런</span> ' +
				((__t = ( HR )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">볼넷</span> ' +
				((__t = ( BB )) == null ? '' : __t) +
				'</li>\n</ul>\n\t';
			} ;
			__p += '\n';
		} else if (TYPE == 'daily_record') { ;
			__p += '\n<h2>일별 기록</h2>\n\t';
			if (IS_PITCHER) { ;
				__p += '\n<ul>\n\t<li><span class="label">이닝</span> ' +
				((__t = ( IP )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">실점</span> ' +
				((__t = ( R )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">피안타</span> ' +
				((__t = ( HIT )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">탈삼진</span> ' +
				((__t = ( SO )) == null ? '' : __t) +
				'</li>\n</ul>\n\t';
			} else { ;
				__p += '\n<ul>\n\t<li><span class="label">타율</span> ' +
				((__t = ( AVG.toFixed(3).replace('0.', '.') )) == null ? '' : __t) +
				'<span class="sub"> (' +
				((__t = ( HIT )) == null ? '' : __t) +
				' /' +
				((__t = ( AB )) == null ? '' : __t) +
				')</span></li>\n\t<li><span class="label">타점</span> ' +
				((__t = ( RBI )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">홈런</span> ' +
				((__t = ( HR )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">사사구</span> ' +
				((__t = ( BBHP )) == null ? '' : __t) +
				'</li>\n</ul>\n\t';
			} ;
			__p += '\n';
		} else if (TYPE == 'monthly_record') { ;
			__p += '\n<h2>' +
			((__t = ( MONTH )) == null ? '' : __t) +
			'월 기록</h2>\n\t';
			if (IS_PITCHER) { ;
				__p += '\n<ul>\n\t<li><span class="label">이닝</span> ' +
				((__t = ( IP )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">평균 자책점</span> ' +
				((__t = ( ERA.toFixed(2) )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">승-패-세</span> ' +
				((__t = ( W )) == null ? '' : __t) +
				'-' +
				((__t = ( L )) == null ? '' : __t) +
				'-' +
				((__t = ( SV )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">피안타율</span> ' +
				((__t = ( HIT_RATIO.toFixed(3).replace('0.', '.') )) == null ? '' : __t) +
				'</li>\n</ul>\n\t';
			} else { ;
				__p += '\n<ul>\n\t<li><span class="label">타율</span> ' +
				((__t = ( AVG.toFixed(3).replace('0.', '.') )) == null ? '' : __t) +
				'<span class="sub"> (' +
				((__t = ( HIT )) == null ? '' : __t) +
				' /' +
				((__t = ( AB )) == null ? '' : __t) +
				')</span></li>\n\t<li><span class="label">타점</span> ' +
				((__t = ( RBI )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">홈런</span> ' +
				((__t = ( HR )) == null ? '' : __t) +
				'</li>\n\t<li><span class="label">볼넷</span> ' +
				((__t = ( BB )) == null ? '' : __t) +
				'</li>\n</ul>\n\t';
			} ;
			__p += '\n';
		} ;
		__p += '\n<div class="comment">' +
		((__t = ( COMMENT )) == null ? '' : __t) +
		'</div>\n';

	}
	return __p
};

this["JST_PRECOMPILE"]["rankCard"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
	function print() { __p += __j.call(arguments, '') }
	with (obj) {
		__p += '<div class="template_comm rank">\n\t<h3 class="card">나의 평점</h3>\n\t<div class="card_template_content">\n\t\t<div class="overview">\n\t\t\t<div class="score">\n\t\t\t\t<div class="stars" style="width: ' +
		((__t = ( 100 / 5 * Number(MY_RANK_POINT))) == null ? '' : __t) +
		'%"></div>\n\t\t\t\t<p class="point">' +
		((__t = ( MY_RANK_POINT.toFixed(1) )) == null ? '' : __t) +
		'</p>\n\t\t\t</div>\n\t\t\t<p class="default_comment ';
		print(AVERAGE_RANK_GUIDE_TEXT ? 'my_comment' : '') ;
		__p += '">';
		print(AVERAGE_RANK_GUIDE_TEXT || '오늘 경기 어땠나요?') ;
		__p += '</p>\n\t\t\t<p class="write">\n\t\t\t\t<button class="';
		print(MY_RANK_POINT ? 'modify' : '') ;
		__p += '">';
		print(MY_RANK_POINT ? '평점수정' : '평점작성') ;
		__p += '</button>\n\t\t\t</p>\n\t\t</div>\n\t\t<form action="">\n\t\t\t<button class="decrease_score">(-)</button>\n\t\t\t<div class="score">\n\t\t\t\t<div class="stars" style="width: 0%"></div>\n\t\t\t</div>\n\t\t\t<button class="increase_score">(+)</button>\n\t\t\t<div class="text_suggest">오늘 경기 어땠나요?</div>\n\t\t\t<div class="text">\n\t\t\t\t<textarea name="" id="" cols="30" rows="10" placeholder="거친 비방보다는 야구팬의 애정을 담은 깨끗한 관전평 부탁드립니다."></textarea>\n\t\t\t\t<span class="count"><span class="ranks-letter-count">0</span> / ' +
		((__t = ( MAX_COMMENT_LENGTH )) == null ? '' : __t) +
		'자</span>\n\t\t\t\t<input class="create" type="button" value="등록">\n\t\t\t</div>\n\t\t</form>\n\t\t<section class="list">\n\t\t\t<p class="netizens"><span>네티즌평</span> <span class="count">' +
		((__t = ( PARTICIPANT_COUNT )) == null ? '' : __t) +
		'명 참여</span></p>\n\t\t\t';

		for (var i = 0, length = RANKS.length; i < RANKS.length; i++) {
			RANK = RANKS[i];
			;
			__p += '\n\t\t\t\t<section class="rank">\n\t\t\t\t\t<div class="score">\n\t\t\t\t\t\t<div class="stars" style="width: ' +
			((__t = ( 100 / 5 * Number(RANK.RANK_POINT) )) == null ? '' : __t) +
			'%"></div>\n\t\t\t\t\t\t<p class="point">' +
			((__t = ( Number(RANK.RANK_POINT).toFixed(1) )) == null ? '' : __t) +
			'</p>\n\t\t\t\t\t</div>\n\n\t\t\t\t\t<p class="comment">';

			print(RANK.COMMENT.substr(0, 60) + '…')
			;
			__p += '</p>\n\n\t\t\t\t\t<p class="user">\n\t\t\t\t\t\t<span class="name">' +
			((__t = ( RANK.USER_ID )) == null ? '' : __t) +
			'</span>\n\t\t\t\t\t\t<span class="date">' +
			((__t = ( RANK.DATE )) == null ? '' : __t) +
			'</span>\n\t\t\t\t\t</p>\n\t\t\t\t</section>\n\t\t\t';

		} 
		;
		__p += '\n\t\t\t<p class="go-list">\n\t\t\t\t<button>전체보기</button>\n\t\t\t</p>\n\t\t</section>\n\t</div>\n</div>';

	}
	return __p
};

this["JST_PRECOMPILE"]["ranks"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
	function print() { __p += __j.call(arguments, '') }
	with (obj) {
		__p += '<header>\n\t<p class="close">\n\t\t<button>닫기</button>\n\t</p>\n\t<div class="overview">\n\t\t<h1>경기 평점</h1>\n\t\t<div class="score">\n\t\t\t<div class="stars" style="width: ' +
		((__t = ( 100 / 5 * Number(AVERAGE_RANK))) == null ? '' : __t) +
		'%"></div>\n\t\t\t<p class="point">' +
		((__t = ( AVERAGE_RANK )) == null ? '' : __t) +
		'</p>\n\t\t</div>\n\t\t<p class="default_comment ';
		print(AVERAGE_RANK_GUIDE_TEXT ? 'my_comment' : '') ;
		__p += '">';
		print(AVERAGE_RANK_GUIDE_TEXT || '별점이 없는 경기') ;
		__p += '</p>\n\t\t<p class="write">\n\t\t\t<button class="';
		print(MY_RANK_POINT ? 'modify' : '') ;
		__p += '">';
		print(MY_RANK_POINT ? '평점수정' : '평점쓰기') ;
		__p += '</button>\n\t\t</p>\n\t</div>\n\t<form action="" style="display:none">\n\t\t<h1>나의 평점</h1>\n\t\t<button class="decrease_score">(-)</button>\n\t\t<div class="score">\n\t\t\t<div class="stars" style="width: 0%"></div>\n\t\t</div>\n\t\t<button class="increase_score">(+)</button>\n\t\t<div class="text_suggest">별점을 선택해주세요</div>\n\t\t<div class="text">\n\t\t\t<textarea name="" id="" cols="30" rows="10" placeholder="거친 비방보다는 야구팬의 애정을 담은 깨끗한 관전평 부탁드립니다."></textarea>\n\t\t\t<span class="count"><span class="ranks-letter-count">0</span> / ' +
		((__t = ( MAX_COMMENT_LENGTH )) == null ? '' : __t) +
		'자</span>\n\t\t\t<input class="delete" type="button" value="삭제">\n\t\t\t<input class="cancel" type="button" value="취소">\n\t\t\t<input class="create" type="button" value="등록">\n\t\t</div>\n\t</form>\n</header>\n\n<section class="list">\n\t<h2><span>네티즌평</span> <span class="count">' +
		((__t = ( PARTICIPANT_COUNT )) == null ? '' : __t) +
		'명 참여</span></h2>\n\t';

		for (var i = 0, length = RANKS.length; i < RANKS.length; i++) {
			RANK = RANKS[i];
			;
			__p += '\n\t\t<section class="rank">\n\t\t\t<div class="score">\n\t\t\t\t<div class="stars" style="width: ' +
			((__t = ( 100 / 5 * Number(RANK.RANK_POINT) )) == null ? '' : __t) +
			'%"></div>\n\t\t\t\t<p class="point">' +
			((__t = ( Number(RANK.RANK_POINT).toFixed(1) )) == null ? '' : __t) +
			'</p>\n\t\t\t</div>\n\n\t\t\t<p class="comment">' +
			((__t = ( RANK.COMMENT )) == null ? '' : __t) +
			'</p>\n\n\t\t\t<p class="user">\n\t\t\t\t<span class="name">';
			print(RANK.USER_ID || '???') ;
			__p += '</span>\n\t\t\t\t<span class="date">' +
			((__t = ( RANK.DATE )) == null ? '' : __t) +
			'</span>\n\t\t\t</p>\n\t\t</section>\n\t';

		} 
		;
		__p += '\n\t<p class="more">\n\t\t<button>더보기 +20</button>\n\t\t<button class="go-top">맨위로</button>\n\t</p>\n</section>\n';

	}
	return __p
};

this["JST_PRECOMPILE"]["result"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
	function print() { __p += __j.call(arguments, '') }
	with (obj) {
		__p += '<div class="template_comm result">\n\t<h3 class="card">경기 결과</h3>\n\t<div class="score">\n\t\t<span class="team_logo away_team" style="background-image: url(' +
		((__t = ( AWAY_TEAM_LOGO )) == null ? '' : __t) +
		')"></span>\n\t\t<em class="result_point away">' +
		((__t = ( AWAY_TEAM_SCORE )) == null ? '' : __t) +
		'</em>\n\t\t<em class="result_point home">' +
		((__t = ( HOME_TEAM_SCORE )) == null ? '' : __t) +
		'</em>\n\t\t<span class="team_logo home_team" style="background-image: url(' +
		((__t = ( HOME_TEAM_LOGO )) == null ? '' : __t) +
		')"></span>\n\t</div>\n\t<div class="recent_stats">\n\t\t<div class="away">\n\t\t\t<p class="team_name">' +
		((__t = ( AWAY_TEAM_NAME )) == null ? '' : __t) +
		'</p>\n\t\t\t';
		if (SHOW_GAME_RANK) { ;
			__p += '\n\t\t\t<div class="separate"></div>\n\t\t\t<p class="change">순위 ' +
			((__t = ( AWAY_TEAM_RANK )) == null ? '' : __t) +
			'위 (' +
			((__t = ( AWAY_TEAM_CHANGE )) == null ? '' : __t) +
			')</p>\n\t\t\t<p class="win-lose">' +
			((__t = ( AWAY_TEAM_WIN )) == null ? '' : __t) +
			'승 ' +
			((__t = ( AWAY_TEAM_DRAW )) == null ? '' : __t) +
			'무 ' +
			((__t = ( AWAY_TEAM_LOSE )) == null ? '' : __t) +
			'패</p>\n\t\t\t<p class="accumulation">연속 ' +
			((__t = ( AWAY_TEAM_STREAK )) == null ? '' : __t) +
			'</p>\n\t\t\t';
		} ;
		__p += '\n\t\t</div>\n\t\t<div class="home">\n\t\t\t<p class="team_name">' +
		((__t = ( HOME_TEAM_NAME )) == null ? '' : __t) +
		'</p>\n\t\t\t';
		if (SHOW_GAME_RANK) { ;
			__p += '\n\t\t\t<p class="change">순위 ' +
			((__t = ( HOME_TEAM_RANK )) == null ? '' : __t) +
			'위 (' +
			((__t = ( HOME_TEAM_CHANGE )) == null ? '' : __t) +
			')</p>\n\t\t\t<p class="win-lose">' +
			((__t = ( HOME_TEAM_WIN )) == null ? '' : __t) +
			'승 ' +
			((__t = ( HOME_TEAM_DRAW )) == null ? '' : __t) +
			'무 ' +
			((__t = ( HOME_TEAM_LOSE )) == null ? '' : __t) +
			'패</p>\n\t\t\t<p class="accumulation">연속 ' +
			((__t = ( HOME_TEAM_STREAK )) == null ? '' : __t) +
			'</p>\n\t\t\t';
		} ;
		__p += '\n\t\t</div>\n\t</div>\n\t<div class="result_board">\n\t\t<table class="tbl tbl_record">\n\t\t\t<thead>\n\t\t\t\t<tr>\n\t\t\t\t\t<th class="team" title="팀"></th>\n\t\t\t\t\t';
		for(var i = 1; i <= LAST_INNING; i++) { ;
			__p += '\n\t\t\t\t\t<th scope="col">' +
			((__t = (i)) == null ? '' : __t) +
			'</th>\n\t\t\t\t\t';
		};
		__p += '\n\t\t\t\t\t<th scope="col" class="space"></th>\n\t\t\t\t\t<th scope="col" title="득점">R</th>\n\t\t\t\t\t<th scope="col" title="안타">H</th>\n\t\t\t\t\t<th scope="col" title="에러">E</th>\n\t\t\t\t\t<th scope="col" title="사사구">B</th>\n\t\t\t\t</tr>\n\t\t\t</thead>\n\t\t\t<tbody>\n\t\t\t\t<tr class="away">\n\t\t\t\t\t<th scope="row">' +
		((__t = ( AWAY_TEAM_NAME )) == null ? '' : __t) +
		'</th>\n\t\t\t\t\t' +
		((__t = ( AWAY_TEAM_SCORE_HTML )) == null ? '' : __t) +
		'\n\t\t\t\t\t<td></td>\n\t\t\t\t\t<td class="run">' +
		((__t = ( AWAY_TEAM_SCORE_RUN )) == null ? '' : __t) +
		'</td>\n\t\t\t\t\t<td class="hit">' +
		((__t = ( AWAY_TEAM_SCORE_HIT )) == null ? '' : __t) +
		'</td>\n\t\t\t\t\t<td class="error">' +
		((__t = ( AWAY_TEAM_SCORE_ERROR )) == null ? '' : __t) +
		'</td>\n\t\t\t\t\t<td class="ballfour">' +
		((__t = ( AWAY_TEAM_SCORE_BALLFOUR )) == null ? '' : __t) +
		'</td>\n\t\t\t\t</tr>\n\t\t\t\t<tr class="home">\n\t\t\t\t\t<th scope="row">' +
		((__t = ( HOME_TEAM_NAME )) == null ? '' : __t) +
		'</th>\n\t\t\t\t\t' +
		((__t = ( HOME_TEAM_SCORE_HTML )) == null ? '' : __t) +
		'\n\t\t\t\t\t<td></td>\n\t\t\t\t\t<td class="run">' +
		((__t = ( HOME_TEAM_SCORE_RUN )) == null ? '' : __t) +
		'</td>\n\t\t\t\t\t<td class="hit">' +
		((__t = ( HOME_TEAM_SCORE_HIT )) == null ? '' : __t) +
		'</td>\n\t\t\t\t\t<td class="error">' +
		((__t = ( HOME_TEAM_SCORE_ERROR )) == null ? '' : __t) +
		'</td>\n\t\t\t\t\t<td class="ballfour">' +
		((__t = ( HOME_TEAM_SCORE_BALLFOUR )) == null ? '' : __t) +
		'</td>\n\t\t\t\t</tr>\n\t\t\t</tbody>\n\t\t</table>\n\t</div>\n\t<div class="background_content" style="background-image: url(' +
		((__t = ( BACKGROUND_IMAGE )) == null ? '' : __t) +
		')"></div>\n</div>\n';

	}
	return __p
};

this["JST_PRECOMPILE"]["scoreboard"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
	function print() { __p += __j.call(arguments, '') }
	with (obj) {
		__p += '<div class="away">\n\t<span class="team_name">' +
		((__t = (AWAY_TEAM_NAME)) == null ? '' : __t) +
		'</span>\n\t<span class="team_logo" style="background-image:url(' +
		((__t = (AWAY_TEAM_M_LOGO)) == null ? '' : __t) +
		')"></span>\n\t<strong title="점수"></strong>\n</div>\n<div class="vs_dot"></div>\n<div class="home">\n\t<strong title="점수"></strong>\n\t<span class="team_logo" style="background-image: url(' +
		((__t = (HOME_TEAM_M_LOGO)) == null ? '' : __t) +
		')"></span>\n\t<span class="team_name">' +
		((__t = (HOME_TEAM_NAME)) == null ? '' : __t) +
		'</span>\n</div>\n';

		var resultInning = INNDATA.info.resultInning || 9,
		isOverTime = (resultInning > 9);
		;
		__p += '\n\n<div class="score_info">\n\t<div class="board_score">\n\t\t<div class="game_team">\n\t\t\t<strong class="screen_out">팀명</strong>\n\t\t\t<span class="txt_team">\n\t\t\t\t<span class="team_logo" style="background-image: url(' +
		((__t = (AWAY_TEAM_LOGO)) == null ? '' : __t) +
		')"></span>\n\t\t\t\t<span class="team_name">' +
		((__t = (AWAY_TEAM_NAME)) == null ? '' : __t) +
		'</span>\n\t\t\t</span>\n\t\t\t<span class="txt_team">\n\t\t\t\t<span class="team_logo" style="background-image: url(' +
		((__t = (HOME_TEAM_LOGO)) == null ? '' : __t) +
		')"></span>\n\t\t\t\t<span class="team_name">' +
		((__t = (HOME_TEAM_NAME)) == null ? '' : __t) +
		'</span>\n\t\t\t</span>\n\t\t</div>\n\t\t<div class="game_score game_extra">\n\t\t\t<div class="score_game">\n\t\t\t\t<div class="wrap_score">\n\t\t\t\t\t<div class="cont_score" id="regular" style="display:block">\n\t\t\t\t\t\t<table class="tbl_score">\n\t\t\t\t\t\t\t<caption class="screen_out">회차별 득점</caption>\n\t\t\t\t\t\t\t<thead>\n\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t';

		for(var i = 1; i <= resultInning; i ++){
			;
			__p += '\n\t\t\t\t\t\t\t\t\t<th scope="col">\n\t\t\t\t\t\t\t\t\t\t' +
			((__t = (i)) == null ? '' : __t) +
			'<span class="screen_out">회</span>\n\t\t\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t\t';

			if(i == 9){
				break;
			}

		};
		;
		__p += '\n\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t</thead>\n\t\t\t\t\t\t\t<tbody>\n\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t';

		for(var a = 1; a <= resultInning; a ++){
			var innData = INNDATA["away"][a],
			innScore = INNDATA["awayScore"][a];

			if(innData){
				;
				__p += '\n\t\t\t\t\t\t\t\t\t<td class="featured" data-inning="' +
				((__t = (innData.inning)) == null ? '' : __t) +
				'" data-half="' +
				((__t = (innData.inningHalf)) == null ? '' : __t) +
				'">\n\t\t\t\t\t\t\t\t\t\t<div class="inner_td">\n\t\t\t\t\t\t\t\t\t\t\t<a href="#none" class="box_score">\n\t\t\t\t\t\t\t\t\t\t\t\t<span>' +
				((__t = (innScore)) == null ? '' : __t) +
				'</span>\n\t\t\t\t\t\t\t\t\t\t\t';

				if(innData.isCritical){
					;
					__p += '\n\t\t\t\t\t\t\t\t\t\t\t\t<strong class="img_highlight ico_decisive">승부처</strong>\n\t\t\t\t\t\t\t\t\t\t\t';

				}
				;
				__p += '\n\t\t\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t\t\t<div class="layer_vod"> <!-- layer_vod의 너비값의 반이 margin-left에 마이너스 값으로 들어갑니다. -->\n\t\t\t\t\t\t\t\t\t\t\t\t<div class="inner_layer">\n\t\t\t\t\t\t\t\t\t\t\t\t\t<ul class="list_vod">\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t';

				_.each(innData.video, function(v, idx){
					var vod = v.DATA.mediaList[0];
					;
					__p += '\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li><a href="#none" class="link_vod" data-id="' +
					((__t = (v.CONTENTS_ID)) == null ? '' : __t) +
					'"><span class="img_highlight ico_vod"></span>' +
					((__t = (vod.title)) == null ? '' : __t) +
					'</a></li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t';

				});
				;
				__p += '\n\t\t\t\t\t\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t\t\t\t\t\t\t<span class="ico_arr"></span>\n\t\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t';

			} else {
				;
				__p += '\n\t\t\t\t\t\t\t\t\t<td data-inning="' +
				((__t = (a)) == null ? '' : __t) +
				'"><div class="box_score"><span>' +
				((__t = (innScore)) == null ? '' : __t) +
				'</span></div></td>\n\t\t\t\t\t\t\t\t';

			}

			if(a == 9){
				break;
			}
		};
		;
		__p += '\n\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t';

		for(var h = 1; h <= resultInning; h++){
			var innData = INNDATA["home"][h],
			innScore = INNDATA["homeScore"][h];

			if(innData){
				;
				__p += '\n\t\t\t\t\t\t\t\t\t<td class="featured" data-inning="' +
				((__t = (innData.inning)) == null ? '' : __t) +
				'" data-half="' +
				((__t = (innData.inningHalf)) == null ? '' : __t) +
				'">\n\t\t\t\t\t\t\t\t\t\t<div class="inner_td">\n\t\t\t\t\t\t\t\t\t\t\t<a href="#none" class="box_score">\n\t\t\t\t\t\t\t\t\t\t\t\t<span>' +
				((__t = (innScore)) == null ? '' : __t) +
				'</span>\n\t\t\t\t\t\t\t\t\t\t\t\t';

				if(innData.isCritical){
					;
					__p += '\n\t\t\t\t\t\t\t\t\t\t\t\t\t<strong class="img_highlight ico_decisive">승부처</strong>\n\t\t\t\t\t\t\t\t\t\t\t\t';

				}
				;
				__p += '\n\t\t\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t\t\t<div class="layer_vod">\n\t\t\t\t\t\t\t\t\t\t\t\t<div class="inner_layer">\n\t\t\t\t\t\t\t\t\t\t\t\t\t<ul class="list_vod">\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t';

				_.each(innData.video, function(v, idx){
					var vod = v.DATA.mediaList[0];
					;
					__p += '\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li><a href="#none" class="link_vod" data-id="' +
					((__t = (v.CONTENTS_ID)) == null ? '' : __t) +
					'"><span class="img_highlight ico_vod"></span>' +
					((__t = (vod.title)) == null ? '' : __t) +
					'</a></li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t';

				});
				;
				__p += '\n\t\t\t\t\t\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t\t\t\t\t\t\t<span class="ico_arr"></span>\n\t\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t';

			} else {
				;
				__p += '\n\t\t\t\t\t\t\t\t\t<td data-inning="' +
				((__t = (h)) == null ? '' : __t) +
				'"><div class="box_score"><span>' +
				((__t = (innScore)) == null ? '' : __t) +
				'</span></div></td>\n\t\t\t\t\t\t\t\t';

			}

			if(h == 9){
				break;
			}
		};
		;
		__p += '\n\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t</tbody>\n\t\t\t\t\t\t</table>\n\t\t\t\t\t</div>\n\t\t\t\t';

		if(isOverTime){
			;
			__p += '\n\t\t\t\t\t<div class="cont_score" id="extra" style="display:none">\n\t\t\t\t\t\t<table class="tbl_score">\n\t\t\t\t\t\t\t<caption class="screen_out">회차별 득점</caption>\n\t\t\t\t\t\t\t<thead>\n\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t\t<th scope="col">\n\t\t\t\t\t\t\t\t\t\t10<span class="screen_out">회</span>\n\t\t\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t\t\t<th scope="col">\n\t\t\t\t\t\t\t\t\t\t11<span class="screen_out">회</span>\n\t\t\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t\t\t<th scope="col">\n\t\t\t\t\t\t\t\t\t\t12<span class="screen_out">회</span>\n\t\t\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t\t\t<th scope="col">\n\t\t\t\t\t\t\t\t\t\t13<span class="screen_out">회</span>\n\t\t\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t\t\t<th scope="col">\n\t\t\t\t\t\t\t\t\t\t14<span class="screen_out">회</span>\n\t\t\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t\t\t<th scope="col">\n\t\t\t\t\t\t\t\t\t\t15<span class="screen_out">회</span>\n\t\t\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t\t\t<th scope="col">\n\t\t\t\t\t\t\t\t\t\t16<span class="screen_out">회</span>\n\t\t\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t\t\t<th scope="col">\n\t\t\t\t\t\t\t\t\t\t17<span class="screen_out">회</span>\n\t\t\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t\t\t<th scope="col">\n\t\t\t\t\t\t\t\t\t\t18<span class="screen_out">회</span>\n\t\t\t\t\t\t\t\t\t</th>\n\t\t\t\t\t\t\t\t</tr>\n\t\t\t\t\t\t\t</thead>\n\t\t\t\t\t\t\t<tbody>\n\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t';

			for(var a = 10; a <= resultInning; a ++){
				var innData = INNDATA["away"][a],
				innScore = INNDATA["awayScore"][a];

				if(innData){
					;
					__p += '\n\t\t\t\t\t\t\t\t\t<td class="featured" data-inning="' +
					((__t = (innData.inning)) == null ? '' : __t) +
					'" data-half="' +
					((__t = (innData.inningHalf)) == null ? '' : __t) +
					'">\n\t\t\t\t\t\t\t\t\t\t<div class="inner_td">\n\t\t\t\t\t\t\t\t\t\t\t<a href="#none" class="box_score">\n\t\t\t\t\t\t\t\t\t\t\t\t<span>' +
					((__t = (innScore)) == null ? '' : __t) +
					'</span>\n\t\t\t\t\t\t\t\t\t\t\t';

					if(innData.isCritical){
						;
						__p += '\n\t\t\t\t\t\t\t\t\t\t\t\t<strong class="img_highlight ico_decisive">승부처</strong>\n\t\t\t\t\t\t\t\t\t\t\t';

					}
					;
					__p += '\n\t\t\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t\t\t<div class="layer_vod">\n\t\t\t\t\t\t\t\t\t\t\t\t<div class="inner_layer">\n\t\t\t\t\t\t\t\t\t\t\t\t\t<ul class="list_vod">\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t';

					_.each(innData.video, function(v, idx){
						var vod = v.DATA.mediaList[0];
						;
						__p += '\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li><a href="#none" class="link_vod" data-id="' +
						((__t = (v.CONTENTS_ID)) == null ? '' : __t) +
						'"><span class="img_highlight ico_vod"></span>' +
						((__t = (vod.title)) == null ? '' : __t) +
						'</a></li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t';

					});
					;
					__p += '\n\t\t\t\t\t\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t\t\t\t\t\t\t<span class="ico_arr"></span>\n\t\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t';

				} else {
					;
					__p += '\n\t\t\t\t\t\t\t\t\t<td data-inning="' +
					((__t = (a)) == null ? '' : __t) +
					'"><div class="box_score"><span>' +
					((__t = (innScore)) == null ? '' : __t) +
					'</span></div></td>\n\t\t\t\t\t\t\t\t';

				}
			};
			;
			__p += '\n\t\t\t\t\t\t\t\t</tr>\n\n\t\t\t\t\t\t\t\t<tr>\n\t\t\t\t\t\t\t\t';

			for(var h = 10; h <= resultInning; h ++){
				var innData = INNDATA["home"][h],
				innScore = INNDATA["homeScore"][h];

				if(innData){
					;
					__p += '\n\t\t\t\t\t\t\t\t\t<td class="featured" data-inning="' +
					((__t = (innData.inning)) == null ? '' : __t) +
					'" data-half="' +
					((__t = (innData.inningHalf)) == null ? '' : __t) +
					'">\n\t\t\t\t\t\t\t\t\t\t<div class="inner_td">\n\t\t\t\t\t\t\t\t\t\t\t<a href="#none" class="box_score">\n\t\t\t\t\t\t\t\t\t\t\t\t<span>' +
					((__t = (innScore)) == null ? '' : __t) +
					'</span>\n\t\t\t\t\t\t\t\t\t\t\t';

					if(innData.isCritical){
						;
						__p += '\n\t\t\t\t\t\t\t\t\t\t\t\t<strong class="img_highlight ico_decisive">승부처</strong>\n\t\t\t\t\t\t\t\t\t\t\t';

					}
					;
					__p += '\n\t\t\t\t\t\t\t\t\t\t\t</a>\n\t\t\t\t\t\t\t\t\t\t\t<div class="layer_vod">\n\t\t\t\t\t\t\t\t\t\t\t\t<div class="inner_layer">\n\t\t\t\t\t\t\t\t\t\t\t\t\t<ul class="list_vod">\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t';

					_.each(innData.video, function(v, idx){
						var vod = v.DATA.mediaList[0];
						;
						__p += '\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<li><a href="#none" class="link_vod" data-id="' +
						((__t = (v.CONTENTS_ID)) == null ? '' : __t) +
						'"><span class="img_highlight ico_vod"></span>' +
						((__t = (vod.title)) == null ? '' : __t) +
						'</a></li>\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t';

					});
					;
					__p += '\n\t\t\t\t\t\t\t\t\t\t\t\t\t</ul>\n\t\t\t\t\t\t\t\t\t\t\t\t\t<span class="ico_arr"></span>\n\t\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t\t\t\t</td>\n\t\t\t\t\t\t\t\t';

				} else {
					;
					__p += '\n\t\t\t\t\t\t\t\t\t<td data-inning="' +
					((__t = (h)) == null ? '' : __t) +
					'"><div class="box_score"><span>' +
					((__t = (innScore)) == null ? '' : __t) +
					'</span></div></td>\n\t\t\t\t\t\t\t\t';

				}
			};
			;
			__p += '\n\t\t\t\t\t\t\t\t</tr>\n\n\t\t\t\t\t\t\t</tbody>\n\t\t\t\t\t\t</table>\n\t\t\t\t\t</div>\n\t\t\t\t';

		}
		;
		__p += '\n\t\t\t\t</div>\n\t\t\t\t';

		if(isOverTime){
			;
			__p += '\n\t\t\t\t\t<button type="button" class="btn_more">\n\t\t\t\t\t\t<span class="img_highlight ico_arr">더보기</span>\n\t\t\t\t\t</button>\n\t\t\t\t';

		}
		;
		__p += '\n\t\t\t</div>\n\t\t</div>\n\n\t\t<div class="game_score2">\n\t\t\t<table class="tbl_score">\n\t\t\t\t<caption class="screen_out">스코어보드</caption>\n\t\t\t\t<thead>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<th scope="col">R</th>\n\t\t\t\t\t</tr>\n\t\t\t\t</thead>\n\t\t\t\t<tbody>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td><div class="box_score" id="awayTotal">0</div></td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td><div class="box_score" id="homeTotal">0</div></td>\n\t\t\t\t\t</tr>\n\t\t\t\t</tbody>\n\t\t\t</table>\n\t\t</div>\n\n\t</div>\n\n</div>';

	}
	return __p
};

this["JST_PRECOMPILE"]["stats"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape, __j = Array.prototype.join;
	function print() { __p += __j.call(arguments, '') }
	with (obj) {
		__p += '<div class="template_comm stats">\n\t<h3 class="card">경기 기록</h3>\n\t<ul class="list_detail">\n\t\t<li class="pitcher_comm pitcher_winner">\n\t\t\t<span class="photo"><img src="' +
		((__t = ( PITCHER_WINNER_IMAGE )) == null ? '' : __t) +
		'" alt="" onerror="this.src=namespace(\'SPORTS_3MIN\').App.PLAYER_NOIMAGE"></span>\n\t\t\t<strong class="badge">승</strong>\n\t\t\t<span class="name">' +
		((__t = ( PITCHER_WINNER_NAME )) == null ? '' : __t) +
		'</span>\n\t\t\t<span class="info">' +
		((__t = ( PITCHER_WINNER_INNING )) == null ? '' : __t) +
		'</span>\n\t\t</li>\n\t\t<li class="pitcher_comm pitcher_loser">\n\t\t\t<span class="photo"><img src="' +
		((__t = ( PITCHER_LOSER_IMAGE )) == null ? '' : __t) +
		'" alt="" onerror="this.src=namespace(\'SPORTS_3MIN\').App.PLAYER_NOIMAGE"></span>\n\t\t\t<strong class="badge">패</strong>\n\t\t\t<span class="name">' +
		((__t = ( PITCHER_LOSER_NAME )) == null ? '' : __t) +
		'</span>\n\t\t\t<span class="info">' +
		((__t = ( PITCHER_LOSER_INNING )) == null ? '' : __t) +
		'</span>\n\t\t</li>\n\t\t';
		if (!NO_SAVE) { ;
			__p += '\n\t\t<li class="pitcher_comm pitcher_save">\n\t\t\t<span class="photo"><img src="' +
			((__t = ( PITCHER_SAVE_IMAGE )) == null ? '' : __t) +
			'" alt="" onerror="this.src=namespace(\'SPORTS_3MIN\').App.PLAYER_NOIMAGE"></span>\n\t\t\t<strong class="badge">세이브</strong>\n\t\t\t<span class="name">' +
			((__t = ( PITCHER_SAVE_NAME )) == null ? '' : __t) +
			'</span>\n\t\t\t<span class="info">' +
			((__t = ( PITCHER_SAVE_INNING )) == null ? '' : __t) +
			'</span>\n\t\t</li>\n\t\t';
		} ;
		__p += '\n\t</ul>\n\n\t<div class="match_team">\n\t\t<div class="away">\n\t\t\t<span class="team_name">' +
		((__t = ( AWAY_TEAM_NAME )) == null ? '' : __t) +
		'</span>\n\t\t\t<span class="team_logo" style="background-image: url(' +
		((__t = ( AWAY_TEAM_LOGO )) == null ? '' : __t) +
		')"></span>\n\t\t</div>\n\t\t<span class="vs_rect"></span>\n\t\t<div class="home">\n\t\t\t<span class="team_name">' +
		((__t = ( HOME_TEAM_NAME )) == null ? '' : __t) +
		'</span>\n\t\t\t<span class="team_logo" style="background-image: url(' +
		((__t = ( HOME_TEAM_LOGO )) == null ? '' : __t) +
		')"></span>\n\t\t</div>\n\t</div>\n\n\t<div class="vs_graph">\n\t\t<div id="positive_stats" class="on">\n\t\t\t<button class="tab" data-tab="positive_stats">기록1</button>\n\t\t\t<ul class="list_record">\n\t\t\t\t';
		for (var i = 0, cnt = GRAPH_DATA_POSITIVE.length; i < cnt; i++) { ;
			__p += '\n\t\t\t\t<li>\n\t\t\t\t\t<span class="txt_cate">' +
			((__t = ( GRAPH_DATA_POSITIVE[i].LABEL )) == null ? '' : __t) +
			'</span>\n\t\t\t\t\t<span class="bg_graph graph_home ' +
			((__t = ( GRAPH_DATA_POSITIVE[i].HOME_STATUS )) == null ? '' : __t) +
			' ' +
			((__t = ( GRAPH_DATA_POSITIVE[i].HOME_COLOR )) == null ? '' : __t) +
			'" data-graph="' +
			((__t = ( GRAPH_DATA_POSITIVE[i].HOME_WIDTH )) == null ? '' : __t) +
			'">\n\t\t\t\t\t\t<span>\n\t\t\t\t\t\t\t' +
			((__t = ( GRAPH_DATA_POSITIVE[i].HOME_VALUE )) == null ? '' : __t) +
			'\n\t\t\t\t\t\t</span>\n\t\t\t\t\t</span>\n\t\t\t\t\t<span class="bg_graph graph_away ' +
			((__t = ( GRAPH_DATA_POSITIVE[i].AWAY_STATUS )) == null ? '' : __t) +
			' ' +
			((__t = ( GRAPH_DATA_POSITIVE[i].AWAY_COLOR )) == null ? '' : __t) +
			'" data-graph="' +
			((__t = ( GRAPH_DATA_POSITIVE[i].AWAY_WIDTH )) == null ? '' : __t) +
			'">\n\t\t\t\t\t\t<span>\n\t\t\t\t\t\t\t' +
			((__t = ( GRAPH_DATA_POSITIVE[i].AWAY_VALUE )) == null ? '' : __t) +
			'\n\t\t\t\t\t\t</span>\n\t\t\t\t\t</span>\n\t\t\t\t</li>\n\t\t\t\t';
		} ;
		__p += '\n\t\t\t</ul>\n\t\t</div>\n\n\t\t<div id="negative_stats">\n\t\t\t<button class="tab" data-tab="negative_stats">기록2</button>\n\t\t\t<ul class="list_record">\n\t\t\t\t';
		for (var i = 0, cnt = GRAPH_DATA_NEGATIVE.length; i < cnt; i++) { ;
			__p += '\n\t\t\t\t<li>\n\t\t\t\t\t<span class="txt_cate">' +
			((__t = ( GRAPH_DATA_NEGATIVE[i].LABEL )) == null ? '' : __t) +
			'</span>\n\t\t\t\t\t<span class="bg_graph graph_home ' +
			((__t = ( GRAPH_DATA_NEGATIVE[i].HOME_STATUS )) == null ? '' : __t) +
			' ' +
			((__t = ( GRAPH_DATA_NEGATIVE[i].HOME_COLOR )) == null ? '' : __t) +
			'" data-graph="' +
			((__t = ( GRAPH_DATA_NEGATIVE[i].HOME_WIDTH )) == null ? '' : __t) +
			'">\n\t\t\t\t\t\t<span>\n\t\t\t\t\t\t\t' +
			((__t = ( GRAPH_DATA_NEGATIVE[i].HOME_VALUE )) == null ? '' : __t) +
			'\n\t\t\t\t\t\t</span>\n\t\t\t\t\t</span>\n\t\t\t\t\t<span class="bg_graph graph_away ' +
			((__t = ( GRAPH_DATA_NEGATIVE[i].AWAY_STATUS )) == null ? '' : __t) +
			' ' +
			((__t = ( GRAPH_DATA_NEGATIVE[i].AWAY_COLOR )) == null ? '' : __t) +
			'" data-graph="' +
			((__t = ( GRAPH_DATA_NEGATIVE[i].AWAY_WIDTH )) == null ? '' : __t) +
			'">\n\t\t\t\t\t\t<span>\n\t\t\t\t\t\t\t' +
			((__t = ( GRAPH_DATA_NEGATIVE[i].AWAY_VALUE )) == null ? '' : __t) +
			'\n\t\t\t\t\t\t</span>\n\t\t\t\t\t</span>\n\t\t\t\t</li>\n\t\t\t\t';
		} ;
		__p += '\n\t\t\t</ul>\n\t\t</div>\n\t</div>\n</div>\n';

	}
	return __p
};

this["JST_PRECOMPILE"]["teamPromotionCard"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape;
	with (obj) {
		__p += '<Style>\n#team-promotion-card-link {\n\theight: 100%\n\twidth: 100%\n\tposition: relative;\n}\n#team-promotion-card-img {\n\tmax-height: 100%;\n\tmax-width: 100%;\n\twidth: auto;\n\theight: auto;\n\tposition: absolute;\n\ttop: 0;\n\tbottom: 0;\n\tleft: 0;\n\tright: 0;\n\tmargin: auto;\n}\n</Style>\n\n<div id="team-promotion-card">\n\t<a href=' +
		((__t = (url)) == null ? '' : __t) +
		' target="_blank" id="team-promotion-card-link">\n\t\t<img src="' +
		((__t = (imageUrl)) == null ? '' : __t) +
		'" id="team-promotion-card-img" alt="' +
		((__t = (_.escape(description))) == null ? '' : __t) +
		'">\n\t</a>\n\t<div class="background_content" style="background-image: url(' +
		((__t = (bgImageUrl)) == null ? '' : __t) +
		')"></div>\n</div>\n';

	}
	return __p
};

this["JST_PRECOMPILE"]["video"] = function(obj) {
	obj || (obj = {});
	var __t, __p = '', __e = _.escape;
	with (obj) {
		__p += '<div class="template_comm video ' +
		((__t = ( PURPOSE )) == null ? '' : __t) +
		'">\n\t<div class="score_board2">\n\t\t<div class="team_away">\n\t\t\t<span class="team_name"></span>\n\t\t\t<span class="team_logo" style="background-image: url(' +
		((__t = (AWAY_LOGO)) == null ? '' : __t) +
		')"></span>\n\t\t\t<strong title="점수">' +
		((__t = (AWAY_SCORE)) == null ? '' : __t) +
		'</strong>\n\t\t</div>\n\t\t<div class="vs_dot">:</div>\n\t\t<div class="team_home">\n\t\t\t<strong title="점수">' +
		((__t = (HOME_SCORE)) == null ? '' : __t) +
		'</strong>\n\t\t\t<span class="team_logo" style="background-image: url(' +
		((__t = (HOME_LOGO)) == null ? '' : __t) +
		')"></span>\n\t\t\t<span class="team_name"></span>\n\t\t</div>\n\t</div>\n\t<div class="highlight_video"></div>\n\t<div class="editor_talk">\n\t\t<h3>' +
		((__t = ( TITLE )) == null ? '' : __t) +
		'</h3>\n\t\t<div class="body">' +
		((__t = ( DESCRIPTION )) == null ? '' : __t) +
		'</div>\n\t</div>\n\n\t<div class="supplement">\n\t\t<div class="inner_supplement">\n\t\t\t<span class="share">\n\t\t\t\t<button><span class="img_highlight"></span>공유</button>\n\t\t\t\t<ul class="non_app_share">\n\t\t\t\t\t<li class="kakaostory">\n\t\t\t\t\t\t<a href="#">카카오스토리 공유하기</a>\n\t\t\t\t\t</li>\n\t\t\t\t\t<li class="twitter">\n\t\t\t\t\t\t<a href="#">트위터 공유하기</a>\n\t\t\t\t\t</li>\n\t\t\t\t\t<li class="facebook">\n\t\t\t\t\t\t<a href="#">페이스북 공유하기</a>\n\t\t\t\t\t</li>\n\t\t\t\t</ul>\n\t\t\t</span>\n\t\t\t<span class="cmt">\n\t\t\t\t<a href="#none" class="link_cmt" data-vid="' +
		((__t = (VIDEO_ID)) == null ? '' : __t) +
		'"></a>\n\t\t\t</span>\n\t\t\t<span class="empathy">\n\t\t\t\t<button>\n\t\t\t\t\t<span class="img_highlight">공감</span>\n\t\t\t\t\t<span class="uoc-icon"></span>\n\t\t\t\t\t<span class="uoc-text">공감</span>\n\t\t\t\t\t<span class="uoc-count">0</span>\n\t\t\t\t</button>\n\t\t\t</span>\n\t\t</div>\n\t</div>\n\n</div>\n';

	}
	return __p
};