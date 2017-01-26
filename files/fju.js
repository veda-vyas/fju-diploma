(function(jQuery){
		function initFlyouts(){
			initPublishedFlyoutMenus(
				[{"id":"288854292384509760","title":"About us","url":"index.html","target":"","nav_menu":false,"nonclickable":false},{"id":"999621893231744982","title":"Teaching Process","url":"teaching-process.html","target":"","nav_menu":false,"nonclickable":false},{"id":"552866978373626961","title":"Learning Process","url":"learning-process.html","target":"","nav_menu":false,"nonclickable":false},{"id":"239738603549033066","title":"Degrees & Programs","url":"degrees--programs.html","target":"","nav_menu":false,"nonclickable":false},{"id":"154980209496661510","title":"Admissions","url":"admissions.html","target":"","nav_menu":false,"nonclickable":false},{"id":"350477275475867026","title":"Contact Us","url":"contact-us.html","target":"","nav_menu":false,"nonclickable":false},{"id":"257552255400159436","title":"Apply Now","url":"http:\/\/apply-973.appspot.com\/apply-pin.html","target":"_blank","nav_menu":false,"nonclickable":false},{"id":"126804662626671551","title":"Teaching Process - Details","url":"teaching-process---details.html","target":"","nav_menu":false,"nonclickable":false},{"id":"651121505615679035","title":"Learning Process - Details","url":"learning-process---details.html","target":"","nav_menu":false,"nonclickable":false},{"id":"278069110193387436","title":"Android Developer Diploma","url":"http:\/\/fju-diploma.appspot.com\/","target":"_blank","nav_menu":false,"nonclickable":false}],
				"288854292384509760",
				'',
				'active',
				false,
				{"navigation\/item":"<li {{#id}}id=\"{{id}}\"{{\/id}} class=\"wsite-menu-item-wrap\">\n\t<a\n\t\t{{^nonclickable}}\n\t\t\t{{^nav_menu}}\n\t\t\t\thref=\"{{url}}\"\n\t\t\t{{\/nav_menu}}\n\t\t{{\/nonclickable}}\n\t\t{{#target}}\n\t\t\ttarget=\"{{target}}\"\n\t\t{{\/target}}\n\t\t{{#membership_required}}\n\t\t\tdata-membership-required=\"{{.}}\"\n\t\t{{\/membership_required}}\n\t\tclass=\"wsite-menu-item\"\n\t\t>\n\t\t{{{title_html}}}\n\t<\/a>\n\t{{#has_children}}{{> navigation\/flyout\/list}}{{\/has_children}}\n<\/li>\n","navigation\/flyout\/list":"<div class=\"wsite-menu-wrap\" style=\"display:none\">\n\t<ul class=\"wsite-menu\">\n\t\t{{#children}}{{> navigation\/flyout\/item}}{{\/children}}\n\t<\/ul>\n<\/div>\n","navigation\/flyout\/item":"<li {{#id}}id=\"{{id}}\"{{\/id}}\n\tclass=\"wsite-menu-subitem-wrap {{#is_current}}wsite-nav-current{{\/is_current}}\"\n\t>\n\t<a\n\t\t{{^nonclickable}}\n\t\t\t{{^nav_menu}}\n\t\t\t\thref=\"{{url}}\"\n\t\t\t{{\/nav_menu}}\n\t\t{{\/nonclickable}}\n\t\t{{#target}}\n\t\t\ttarget=\"{{target}}\"\n\t\t{{\/target}}\n\t\tclass=\"wsite-menu-subitem\"\n\t\t>\n\t\t<span class=\"wsite-menu-title\">\n\t\t\t{{{title_html}}}\n\t\t<\/span>{{#has_children}}<span class=\"wsite-menu-arrow\">&gt;<\/span>{{\/has_children}}\n\t<\/a>\n\t{{#has_children}}{{> navigation\/flyout\/list}}{{\/has_children}}\n<\/li>\n"},
				{}
			)
		}
		if (jQuery) {
			jQuery(document).ready(function() { jQuery(initFlyouts); });
		}else{
			if (Prototype.Browser.IE) window.onload = initFlyouts;
			else document.observe('dom:loaded', initFlyouts);
		}
	})(window._W && _W.jQuery)