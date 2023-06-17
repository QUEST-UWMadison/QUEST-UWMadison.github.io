---
title: "QUEST - Home"
layout: homelay
excerpt: "QUEST - UW Madison"
sitemap: false
permalink: /
---

Welcome to the official website of QUEST, we are Quantum and Emerging Systems and Architecture group at the University of Wisconsin-Madison! Our team explores a wide range of disciplines within system and architectural design, quantum computing, hardware security, and sustainability. We are interested in developing new abstractions, architectures, and tools for quantum and classical computing systems. 


<!-- **Look at the current [team]({{ site.url }}{{ site.baseurl }}/team) **!** -->


## Selected Publications

{% for publi in site.data.publist %}
  {% if publi.selected == 1 %}
  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br />
  <a href="{{ publi.link.url }}">{{ publi.link.display }}</a> | <a href="{{ publi.link.pdf }}"> PDF </a> | 
  <a href="{{ publi.link.slides }}"> Slides </a>
  {% endif %}

  {% if publi.selected == 2 %}
  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br />
  <a href="{{ publi.link.url }}">{{ publi.link.display }}</a> | <a href="{{ publi.link.pdf }}"> PDF </a> 
  {% endif %}

{% endfor %}

<!-- <figure class="fourth">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/Logo_Leiden.jpg" style="width: 210px">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/Logo_Nanofront.jpg" style="width: 110px">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/Logo_NWO.jpg" style="width: 120px">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/Logo_ERC.jpg" style="width: 110px">
</figure> -->
