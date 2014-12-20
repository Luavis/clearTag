import cleartag

clear = cleartag.ClearTag();
cleared_data = clear.clear_tag("""
	<script>alert("asdfsg")</script>
	<style>alert("Hello World")</style>
	<iframe src="naver.com">
	</iframe>
	<a onclick="javascript:alert("Hello World")" href="google.com">
	<x:xml>Test</x:xml>
	<div style="width: behaviour(./ads.htc)"></div>
	<div style="-moz-binding: url(./ads.htc)"></div>
	<div style="width: expression(./ads.htc)"></div>
	<p></p>
	<img src="google.com">
	""")

print(cleared_data)