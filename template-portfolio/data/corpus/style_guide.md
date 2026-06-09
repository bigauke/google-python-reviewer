Title: Live Content

Description: Fetched live

Source: https://google.github.io/styleguide/pyguide.html

---

<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Begin Jekyll SEO tag v2.8.0 -->
<title>styleguide | Style guides for Google-originated open-source projects</title>
<meta name="generator" content="Jekyll v3.10.0" />
<meta property="og:title" content="styleguide" />
<meta property="og:locale" content="en_US" />
<meta name="description" content="Style guides for Google-originated open-source projects" />
<meta property="og:description" content="Style guides for Google-originated open-source projects" />
<link rel="canonical" href="https://google.github.io/styleguide/pyguide.html" />
<meta property="og:url" content="https://google.github.io/styleguide/pyguide.html" />
<meta property="og:site_name" content="styleguide" />
<meta property="og:type" content="website" />
<meta name="twitter:card" content="summary" />
<meta property="twitter:title" content="styleguide" />
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"WebPage","description":"Style guides for Google-originated open-source projects","headline":"styleguide","url":"https://google.github.io/styleguide/pyguide.html"}</script>
<!-- End Jekyll SEO tag -->

    <link rel="stylesheet" href="/styleguide/assets/css/style.css?v=1809c769de31ba388c755ad15dd057a9ba8531fd">
    <link rel="shortcut icon" type="image/x-icon" href="/styleguide/favicon.ico">

  </head>
  <body>
    <div class="container-lg px-3 my-5 markdown-body">
      
      <h1><a href="https://google.github.io/styleguide/">styleguide</a></h1>
      

      <!--
AUTHORS:
Prefer only GitHub-flavored Markdown in external text.
See README.md for details.
-->

<h1 id="google-python-style-guide">Google Python Style Guide</h1>

<!-- markdown="1" is required for GitHub Pages to render the TOC properly. -->

<details>
  <summary>Table of Contents</summary>

  <ul>
    <li><a href="#s1-background">1 Background</a></li>
    <li><a href="#s2-python-language-rules">2 Python Language Rules</a>
      <ul>
        <li><a href="#s2.1-lint">2.1 Lint</a></li>
        <li><a href="#s2.2-imports">2.2 Imports</a></li>
        <li><a href="#s2.3-packages">2.3 Packages</a></li>
        <li><a href="#s2.4-exceptions">2.4 Exceptions</a></li>
        <li><a href="#s2.5-global-variables">2.5 Mutable Global State</a></li>
        <li><a href="#s2.6-nested">2.6 Nested/Local/Inner Classes and Functions</a></li>
        <li><a href="#s2.7-comprehensions">2.7 Comprehensions &amp; Generator Expressions</a></li>
        <li><a href="#s2.8-default-iterators-and-operators">2.8 Default Iterators and Operators</a></li>
        <li><a href="#s2.9-generators">2.9 Generators</a></li>
        <li><a href="#s2.10-lambda-functions">2.10 Lambda Functions</a></li>
        <li><a href="#s2.11-conditional-expressions">2.11 Conditional Expressions</a></li>
        <li><a href="#s2.12-default-argument-values">2.12 Default Argument Values</a></li>
        <li><a href="#s2.13-properties">2.13 Properties</a></li>
        <li><a href="#s2.14-truefalse-evaluations">2.14 True/False Evaluations</a></li>
        <li><a href="#s2.16-lexical-scoping">2.16 Lexical Scoping</a></li>
        <li><a href="#s2.17-function-and-method-decorators">2.17 Function and Method Decorators</a></li>
        <li><a href="#s2.18-threading">2.18 Threading</a></li>
        <li><a href="#s2.19-power-features">2.19 Power Features</a></li>
        <li><a href="#s2.20-modern-python">2.20 Modern Python: from __future__ imports</a></li>
        <li><a href="#s2.21-type-annotated-code">2.21 Type Annotated Code</a></li>
      </ul>
    </li>
    <li><a href="#s3-python-style-rules">3 Python Style Rules</a>
      <ul>
        <li><a href="#s3.1-semicolons">3.1 Semicolons</a></li>
        <li><a href="#s3.2-line-length">3.2 Line length</a></li>
        <li><a href="#s3.3-parentheses">3.3 Parentheses</a></li>
        <li><a href="#s3.4-indentation">3.4 Indentation</a>
          <ul>
            <li><a href="#s3.4.1-trailing-commas">3.4.1 Trailing commas in sequences of items?</a></li>
          </ul>
        </li>
        <li><a href="#s3.5-blank-lines">3.5 Blank Lines</a></li>
        <li><a href="#s3.6-whitespace">3.6 Whitespace</a></li>
        <li><a href="#s3.7-shebang-line">3.7 Shebang Line</a></li>
        <li><a href="#s3.8-comments-and-docstrings">3.8 Comments and Docstrings</a>
          <ul>
            <li><a href="#s3.8.1-comments-in-doc-strings">3.8.1 Docstrings</a></li>
            <li><a href="#s3.8.2-comments-in-modules">3.8.2 Modules</a></li>
            <li><a href="#s3.8.2.1-test-modules">3.8.2.1 Test modules</a></li>
            <li><a href="#s3.8.3-functions-and-methods">3.8.3 Functions and Methods</a></li>
            <li><a href="#s3.8.3.1-overridden-methods">3.8.3.1 Overridden Methods</a></li>
            <li><a href="#s3.8.4-comments-in-classes">3.8.4 Classes</a></li>
            <li><a href="#s3.8.5-block-and-inline-comments">3.8.5 Block and Inline Comments</a></li>
            <li><a href="#s3.8.6-punctuation-spelling-and-grammar">3.8.6 Punctuation, Spelling, and Grammar</a></li>
          </ul>
        </li>
        <li><a href="#s3.10-strings">3.10 Strings</a>
          <ul>
            <li><a href="#s3.10.1-logging">3.10.1 Logging</a></li>
            <li><a href="#s3.10.2-error-messages">3.10.2 Error Messages</a></li>
          </ul>
        </li>
        <li><a href="#s3.11-files-sockets-closeables">3.11 Files, Sockets, and similar Stateful Resources</a></li>
        <li><a href="#s3.12-todo-comments">3.12 TODO Comments</a></li>
        <li><a href="#s3.13-imports-formatting">3.13 Imports formatting</a></li>
        <li><a href="#s3.14-statements">3.14 Statements</a></li>
        <li><a href="#s3.15-accessors">3.15 Accessors</a></li>
        <li><a href="#s3.16-naming">3.16 Naming</a>
          <ul>
            <li><a href="#s3.16.1-names-to-avoid">3.16.1 Names to Avoid</a></li>
            <li><a href="#s3.16.2-naming-conventions">3.16.2 Naming Conventions</a></li>
            <li><a href="#s3.16.3-file-naming">3.16.3 File Naming</a></li>
            <li><a href="#s3.16.4-guidelines-derived-from-guidos-recommendations">3.16.4 Guidelines derived from Guido’s Recommendations</a></li>
          </ul>
        </li>
        <li><a href="#s3.17-main">3.17 Main</a></li>
        <li><a href="#s3.18-function-length">3.18 Function length</a></li>
        <li><a href="#s3.19-type-annotations">3.19 Type Annotations</a>
          <ul>
            <li><a href="#s3.19.1-general-rules">3.19.1 General Rules</a></li>
            <li><a href="#s3.19.2-line-breaking">3.19.2 Line Breaking</a></li>
            <li><a href="#s3.19.3-forward-declarations">3.19.3 Forward Declarations</a></li>
            <li><a href="#s3.19.4-default-values">3.19.4 Default Values</a></li>
            <li><a href="#s3.19.5-nonetype">3.19.5 NoneType</a></li>
            <li><a href="#s3.19.6-type-aliases">3.19.6 Type Aliases</a></li>
            <li><a href="#s3.19.7-ignoring-types">3.19.7 Ignoring Types</a></li>
            <li><a href="#s3.19.8-typing-variables">3.19.8 Typing Variables</a></li>
            <li><a href="#s3.19.9-tuples-vs-lists">3.19.9 Tuples vs Lists</a></li>
            <li><a href="#s3.19.10-typevars">3.19.10 Type variables</a></li>
            <li><a href="#s3.19.11-string-types">3.19.11 String types</a></li>
            <li><a href="#s3.19.12-imports-for-typing">3.19.12 Imports For Typing</a></li>
            <li><a href="#s3.19.13-conditional-imports">3.19.13 Conditional Imports</a></li>
            <li><a href="#s3.19.14-circular-dependencies">3.19.14 Circular Dependencies</a></li>
            <li><a href="#s3.19.15-generics">3.19.15 Generics</a></li>
            <li><a href="#s3.19.16-build-dependencies">3.19.16 Build Dependencies</a></li>
          </ul>
        </li>
      </ul>
    </li>
    <li><a href="#4-parting-words">4 Parting Words</a></li>
  </ul>

</details>

<p><a id="s1-background"></a>
<a id="1-background"></a></p>

<p><a id="background"></a></p>
<h2 id="1-background">1 Background</h2>

<p>Python is the main dynamic language used at Google. This style guide is a list
of <em>dos and don’ts</em> for Python programs.</p>

<p>To help you format code correctly, we’ve created a <a href="/styleguide/google_python_style.vim">settings file for Vim</a>. For Emacs, the default settings should be fine.</p>

<p>Many teams use the <a href="https://github.com/psf/black">Black</a> or <a href="https://github.com/google/pyink">Pyink</a>
auto-formatter to avoid arguing over formatting.</p>

<p><a id="s2-python-language-rules"></a>
<a id="2-python-language-rules"></a></p>

<p><a id="python-language-rules"></a></p>
<h2 id="2-python-language-rules">2 Python Language Rules</h2>

<p><a id="s2.1-lint"></a>
<a id="21-lint"></a></p>

<p><a id="lint"></a></p>
<h3 id="21-lint">2.1 Lint</h3>

<p>Run <code class="language-plaintext highlighter-rouge">pylint</code> over your code using this <a href="https://google.github.io/styleguide/pylintrc">pylintrc</a>.</p>

<p><a id="s2.1.1-definition"></a>
<a id="211-definition"></a></p>

<p><a id="lint-definition"></a></p>
<h4 id="211-definition">2.1.1 Definition</h4>

<p><code class="language-plaintext highlighter-rouge">pylint</code>
is a tool for finding bugs and style problems in Python source code. It finds
problems that are typically caught by a compiler for less dynamic languages like
C and C++. Because of the dynamic nature of Python, some
warnings may be incorrect; however, spurious warnings should be fairly
infrequent.</p>

<p><a id="s2.1.2-pros"></a>
<a id="212-pros"></a></p>

<p><a id="lint-pros"></a></p>
<h4 id="212-pros">2.1.2 Pros</h4>

<p>Catches easy-to-miss errors like typos, using-vars-before-assignment, etc.</p>

<p><a id="s2.1.3-cons"></a>
<a id="213-cons"></a></p>

<p><a id="lint-cons"></a></p>
<h4 id="213-cons">2.1.3 Cons</h4>

<p><code class="language-plaintext highlighter-rouge">pylint</code>
isn’t perfect. To take advantage of it, sometimes we’ll need to write around it,
suppress its warnings or fix it.</p>

<p><a id="s2.1.4-decision"></a>
<a id="214-decision"></a></p>

<p><a id="lint-decision"></a></p>
<h4 id="214-decision">2.1.4 Decision</h4>

<p>Make sure you run
<code class="language-plaintext highlighter-rouge">pylint</code>
on your code.</p>

<p>Suppress warnings if they are inappropriate so that other issues are not hidden.
To suppress warnings, you can set a line-level comment:</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">def</span> <span class="nf">do_PUT</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>  <span class="c1"># WSGI name, so pylint: disable=invalid-name
</span>  <span class="p">...</span>
</code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">pylint</code>
warnings are each identified by symbolic name (<code class="language-plaintext highlighter-rouge">empty-docstring</code>)
Google-specific warnings start with <code class="language-plaintext highlighter-rouge">g-</code>.</p>

<p>If the reason for the suppression is not clear from the symbolic name, add an
explanation.</p>

<p>Suppressing in this way has the advantage that we can easily search for
suppressions and revisit them.</p>

<p>You can get a list of
<code class="language-plaintext highlighter-rouge">pylint</code>
warnings by doing:</p>

<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code>pylint <span class="nt">--list-msgs</span>
</code></pre></div></div>

<p>To get more information on a particular message, use:</p>

<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code>pylint <span class="nt">--help-msg</span><span class="o">=</span>invalid-name
</code></pre></div></div>

<p>Prefer <code class="language-plaintext highlighter-rouge">pylint: disable</code> to the deprecated older form <code class="language-plaintext highlighter-rouge">pylint: disable-msg</code>.</p>

<p>Unused argument warnings can be suppressed by deleting the variables at the
beginning of the function. Always include a comment explaining why you are
deleting it. “Unused.” is sufficient. For example:</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">def</span> <span class="nf">viking_cafe_order</span><span class="p">(</span><span class="n">spam</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">beans</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">eggs</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="bp">None</span> <span class="o">=</span> <span class="bp">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
    <span class="k">del</span> <span class="n">beans</span><span class="p">,</span> <span class="n">eggs</span>  <span class="c1"># Unused by vikings.
</span>    <span class="k">return</span> <span class="n">spam</span> <span class="o">+</span> <span class="n">spam</span> <span class="o">+</span> <span class="n">spam</span>
</code></pre></div></div>

<p>Other common forms of suppressing this warning include using ‘<code class="language-plaintext highlighter-rouge">_</code>’ as the
identifier for the unused argument or prefixing the argument name with
‘<code class="language-plaintext highlighter-rouge">unused_</code>’, or assigning them to ‘<code class="language-plaintext highlighter-rouge">_</code>’. These forms are allowed but no longer
encouraged. These break callers that pass arguments by name and do not enforce
that the arguments are actually unused.</p>

<p><a id="s2.2-imports"></a>
<a id="22-imports"></a></p>

<p><a id="imports"></a></p>
<h3 id="22-imports">2.2 Imports</h3>

<p>Use <code class="language-plaintext highlighter-rouge">import</code> statements for packages and modules only, not for individual types,
classes, or functions.</p>

<p><a id="s2.2.1-definition"></a>
<a id="221-definition"></a></p>

<p><a id="imports-definition"></a></p>
<h4 id="221-definition">2.2.1 Definition</h4>

<p>Reusability mechanism for sharing code from one module to another.</p>

<p><a id="s2.2.2-pros"></a>
<a id="222-pros"></a></p>

<p><a id="imports-pros"></a></p>
<h4 id="222-pros">2.2.2 Pros</h4>

<p>The namespace management convention is simple. The source of each identifier is
indicated in a consistent way; <code class="language-plaintext highlighter-rouge">x.Obj</code> says that object <code class="language-plaintext highlighter-rouge">Obj</code> is defined in
module <code class="language-plaintext highlighter-rouge">x</code>.</p>

<p><a id="s2.2.3-cons"></a>
<a id="223-cons"></a></p>

<p><a id="imports-cons"></a></p>
<h4 id="223-cons">2.2.3 Cons</h4>

<p>Module names can still collide. Some module names are inconveniently long.</p>

<p><a id="s2.2.4-decision"></a>
<a id="224-decision"></a></p>

<p><a id="imports-decision"></a></p>
<h4 id="224-decision">2.2.4 Decision</h4>

<ul>
  <li>Use <code class="language-plaintext highlighter-rouge">import x</code> for importing packages and modules.</li>
  <li>Use <code class="language-plaintext highlighter-rouge">from x import y</code> where <code class="language-plaintext highlighter-rouge">x</code> is the package prefix and <code class="language-plaintext highlighter-rouge">y</code> is the module
name with no prefix.</li>
  <li>Use <code class="language-plaintext highlighter-rouge">from x import y as z</code> in any of the following circumstances:
    <ul>
      <li>Two modules named <code class="language-plaintext highlighter-rouge">y</code> are to be imported.</li>
      <li><code class="language-plaintext highlighter-rouge">y</code> conflicts with a top-level name defined in the current module.</li>
      <li><code class="language-plaintext highlighter-rouge">y</code> conflicts with a common parameter name that is part of the public
API (e.g., <code class="language-plaintext highlighter-rouge">features</code>).</li>
      <li><code class="language-plaintext highlighter-rouge">y</code> is an inconveniently long name.</li>
      <li><code class="language-plaintext highlighter-rouge">y</code> is too generic in the context of your code (e.g., <code class="language-plaintext highlighter-rouge">from
storage.file_system import options as fs_options</code>).</li>
    </ul>
  </li>
  <li>Use <code class="language-plaintext highlighter-rouge">import y as z</code> only when <code class="language-plaintext highlighter-rouge">z</code> is a standard abbreviation (e.g., <code class="language-plaintext highlighter-rouge">import
numpy as np</code>).</li>
</ul>

<p>For example the module <code class="language-plaintext highlighter-rouge">sound.effects.echo</code> may be imported as follows:</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kn">from</span> <span class="nn">sound.effects</span> <span class="kn">import</span> <span class="n">echo</span>
<span class="p">...</span>
<span class="n">echo</span><span class="p">.</span><span class="n">EchoFilter</span><span class="p">(</span><span class="nb">input</span><span class="p">,</span> <span class="n">output</span><span class="p">,</span> <span class="n">delay</span><span class="o">=</span><span class="mf">0.7</span><span class="p">,</span> <span class="n">atten</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
</code></pre></div></div>

<p>Do not use relative names in imports. Even if the module is in the same package,
use the full package name. This helps prevent unintentionally importing a
package twice.</p>

<p><a id="imports-exemptions"></a></p>
<h5 id="2241-exemptions">2.2.4.1 Exemptions</h5>

<p>Exemptions from this rule:</p>

<ul>
  <li>Symbols from the following modules are used to support static analysis and
type checking:
    <ul>
      <li><a href="#typing-imports"><code class="language-plaintext highlighter-rouge">typing</code> module</a></li>
      <li><a href="#typing-imports"><code class="language-plaintext highlighter-rouge">collections.abc</code> module</a></li>
      <li><a href="https://github.com/python/typing_extensions/blob/main/README.md"><code class="language-plaintext highlighter-rouge">typing_extensions</code> module</a></li>
    </ul>
  </li>
  <li>Redirects from the
<a href="https://six.readthedocs.io/#module-six.moves">six.moves module</a>.</li>
</ul>

<p><a id="s2.3-packages"></a>
<a id="23-packages"></a></p>

<p><a id="packages"></a></p>
<h3 id="23-packages">2.3 Packages</h3>

<p>Import each module using the full pathname location of the module.</p>

<p><a id="s2.3.1-pros"></a>
<a id="231-pros"></a></p>

<p><a id="packages-pros"></a></p>
<h4 id="231-pros">2.3.1 Pros</h4>

<p>Avoids conflicts in module names or incorrect imports due to the module search
path not being what the author expected. Makes it easier to find modules.</p>

<p><a id="s2.3.2-cons"></a>
<a id="232-cons"></a></p>

<p><a id="packages-cons"></a></p>
<h4 id="232-cons">2.3.2 Cons</h4>

<p>Makes it harder to deploy code because you have to replicate the package
hierarchy. Not really a problem with modern deployment mechanisms.</p>

<p><a id="s2.3.3-decision"></a>
<a id="233-decision"></a></p>

<p><a id="packages-decision"></a></p>
<h4 id="233-decision">2.3.3 Decision</h4>

<p>All new code should import each module by its full package name.</p>

<p>Imports should be as follows:</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">Yes</span><span class="p">:</span>
  <span class="c1"># Reference absl.flags in code with the complete name (verbose).
</span>  <span class="kn">import</span> <span class="nn">absl.flags</span>
  <span class="kn">from</span> <span class="nn">doctor.who</span> <span class="kn">import</span> <span class="n">jodie</span>

  <span class="n">_FOO</span> <span class="o">=</span> <span class="n">absl</span><span class="p">.</span><span class="n">flags</span><span class="p">.</span><span class="n">DEFINE_string</span><span class="p">(...)</span>
</code></pre></div></div>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">Yes</span><span class="p">:</span>
  <span class="c1"># Reference flags in code with just the module name (common).
</span>  <span class="kn">from</span> <span class="nn">absl</span> <span class="kn">import</span> <span class="n">flags</span>
  <span class="kn">from</span> <span class="nn">doctor.who</span> <span class="kn">import</span> <span class="n">jodie</span>

  <span class="n">_FOO</span> <span class="o">=</span> <span class="n">flags</span><span class="p">.</span><span class="n">DEFINE_string</span><span class="p">(...)</span>
</code></pre></div></div>

<p><em>(assume this file lives in <code class="language-plaintext highlighter-rouge">doctor/who/</code> where <code class="language-plaintext highlighter-rouge">jodie.py</code> also exists)</em></p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">No</span><span class="p">:</span>
  <span class="c1"># Unclear what module the author wanted and what will be imported.  The actual
</span>  <span class="c1"># import behavior depends on external factors controlling sys.path.
</span>  <span class="c1"># Which possible jodie module did the author intend to import?
</span>  <span class="kn">import</span> <span class="nn">jodie</span>
</code></pre></div></div>

<p>The directory the main binary is located in should not be assumed to be in
<code class="language-plaintext highlighter-rouge">sys.path</code> despite that happening in some environments. This being the case,
code should assume that <code class="language-plaintext highlighter-rouge">import jodie</code> refers to a third-party or top-level
package named <code class="language-plaintext highlighter-rouge">jodie</code>, not a local <code class="language-plaintext highlighter-rouge">jodie.py</code>.</p>

<p><a id="s2.4-exceptions"></a>
<a id="24-exceptions"></a></p>

<p><a id="exceptions"></a></p>
<h3 id="24-exceptions">2.4 Exceptions</h3>

<p>Exceptions are allowed but must be used carefully.</p>

<p><a id="s2.4.1-definition"></a>
<a id="241-definition"></a></p>

<p><a id="exceptions-definition"></a></p>
<h4 id="241-definition">2.4.1 Definition</h4>

<p>Exceptions are a means of breaking out of normal control flow to handle errors
or other exceptional conditions.</p>

<p><a id="s2.4.2-pros"></a>
<a id="242-pros"></a></p>

<p><a id="exceptions-pros"></a></p>
<h4 id="242-pros">2.4.2 Pros</h4>

<p>The control flow of normal operation code is not cluttered by error-handling
code. It also allows the control flow to skip multiple frames when a certain
condition occurs, e.g., returning from N nested functions in one step instead of
having to plumb error codes through.</p>

<p><a id="s2.4.3-cons"></a>
<a id="243-cons"></a></p>

<p><a id="exceptions-cons"></a></p>
<h4 id="243-cons">2.4.3 Cons</h4>

<p>May cause the control flow to be confusing. Easy to miss error cases when making
library calls.</p>

<p><a id="s2.4.4-decision"></a>
<a id="244-decision"></a></p>

<p><a id="exceptions-decision"></a></p>
<h4 id="244-decision">2.4.4 Decision</h4>

<p>Exceptions must follow certain conditions:</p>

<ul>
  <li>
    <p>Make use of built-in exception classes when it makes sense. For example,
raise a <code class="language-plaintext highlighter-rouge">ValueError</code> to indicate a programming mistake like a violated
precondition, such as may happen when validating function arguments.</p>
  </li>
  <li>
    <p>Do not use <code class="language-plaintext highlighter-rouge">assert</code> statements in place of conditionals or validating
preconditions. They must not be critical to the application logic. A litmus
test would be that the <code class="language-plaintext highlighter-rouge">assert</code> could be removed without breaking the code.
<code class="language-plaintext highlighter-rouge">assert</code> conditionals are
<a href="https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement">not guaranteed</a>
to be evaluated. For <a href="https://pytest.org">pytest</a> based tests, <code class="language-plaintext highlighter-rouge">assert</code> is
okay and expected to verify expectations. For
example:</p>

    <div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">Yes</span><span class="p">:</span>
  <span class="k">def</span> <span class="nf">connect_to_next_port</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">minimum</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
    <span class="s">"""Connects to the next available port.

    Args:
      minimum: A port value greater or equal to 1024.

    Returns:
      The new minimum port.

    Raises:
      ConnectionError: If no available port is found.
    """</span>
    <span class="k">if</span> <span class="n">minimum</span> <span class="o">&lt;</span> <span class="mi">1024</span><span class="p">:</span>
      <span class="c1"># Note that this raising of ValueError is not mentioned in the doc
</span>      <span class="c1"># string's "Raises:" section because it is not appropriate to
</span>      <span class="c1"># guarantee this specific behavioral reaction to API misuse.
</span>      <span class="k">raise</span> <span class="nb">ValueError</span><span class="p">(</span><span class="sa">f</span><span class="s">'Min. port must be at least 1024, not </span><span class="si">{</span><span class="n">minimum</span><span class="si">}</span><span class="s">.'</span><span class="p">)</span>
    <span class="n">port</span> <span class="o">=</span> <span class="bp">self</span><span class="p">.</span><span class="n">_find_next_open_port</span><span class="p">(</span><span class="n">minimum</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">port</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
      <span class="k">raise</span> <span class="nb">ConnectionError</span><span class="p">(</span>
          <span class="sa">f</span><span class="s">'Could not connect to service on port </span><span class="si">{</span><span class="n">minimum</span><span class="si">}</span><span class="s"> or higher.'</span><span class="p">)</span>
    <span class="c1"># The code does not depend on the result of this assert.
</span>    <span class="k">assert</span> <span class="n">port</span> <span class="o">&gt;=</span> <span class="n">minimum</span><span class="p">,</span> <span class="p">(</span>
        <span class="sa">f</span><span class="s">'Unexpected port </span><span class="si">{</span><span class="n">port</span><span class="si">}</span><span class="s"> when minimum was </span><span class="si">{</span><span class="n">minimum</span><span class="si">}</span><span class="s">.'</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">port</span>
</code></pre></div>    </div>

    <div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">No</span><span class="p">:</span>
  <span class="k">def</span> <span class="nf">connect_to_next_port</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">minimum</span><span class="p">:</span> <span class="nb">int</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">int</span><span class="p">:</span>
    <span class="s">"""Connects to the next available port.

    Args:
      minimum: A port value greater or equal to 1024.

    Returns:
      The new minimum port.
    """</span>
    <span class="k">assert</span> <span class="n">minimum</span> <span class="o">&gt;=</span> <span class="mi">1024</span><span class="p">,</span> <span class="s">'Minimum port must be at least 1024.'</span>
    <span class="c1"># The following code depends on the previous assert.
</span>    <span class="n">port</span> <span class="o">=</span> <span class="bp">self</span><span class="p">.</span><span class="n">_find_next_open_port</span><span class="p">(</span><span class="n">minimum</span><span class="p">)</span>
    <span class="k">assert</span> <span class="n">port</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span>
    <span class="c1"># The type checking of the return statement relies on the assert.
</span>    <span class="k">return</span> <span class="n">port</span>
</code></pre></div>    </div>
  </li>
  <li>
    <p>Libraries or packages may define their own exceptions. When doing so they
must inherit from an existing exception class. Exception names should end in
<code class="language-plaintext highlighter-rouge">Error</code> and should not introduce repetition (<code class="language-plaintext highlighter-rouge">foo.FooError</code>).</p>
  </li>
  <li>
    <p>Never use catch-all <code class="language-plaintext highlighter-rouge">except:</code> statements, or catch <code class="language-plaintext highlighter-rouge">Exception</code> or
<code class="language-plaintext highlighter-rouge">StandardError</code>, unless you are</p>

    <ul>
      <li>re-raising the exception, or</li>
      <li>creating an isolation point in the program where exceptions are not
propagated but are recorded and suppressed instead, such as protecting a
thread from crashing by guarding its outermost block.</li>
    </ul>

    <p>Python is very tolerant in this regard and <code class="language-plaintext highlighter-rouge">except:</code> will really catch
everything including misspelled names, sys.exit() calls, Ctrl+C interrupts,
unittest failures and all kinds of other exceptions that you simply don’t
want to catch.</p>
  </li>
  <li>
    <p>Minimize the amount of code in a <code class="language-plaintext highlighter-rouge">try</code>/<code class="language-plaintext highlighter-rouge">except</code> block. The larger the body
of the <code class="language-plaintext highlighter-rouge">try</code>, the more likely that an exception will be raised by a line of
code that you didn’t expect to raise an exception. In those cases, the
<code class="language-plaintext highlighter-rouge">try</code>/<code class="language-plaintext highlighter-rouge">except</code> block hides a real error.</p>
  </li>
  <li>
    <p>Use the <code class="language-plaintext highlighter-rouge">finally</code> clause to execute code whether or not an exception is
raised in the <code class="language-plaintext highlighter-rouge">try</code> block. This is often useful for cleanup, i.e., closing a
file.</p>
  </li>
</ul>

<p><a id="s2.5-global-variables"></a>
<a id="25-global-variables"></a>
<a id="s2.5-global-state"></a>
<a id="25-global-state"></a></p>

<p><a id="global-variables"></a></p>
<h3 id="25-mutable-global-state">2.5 Mutable Global State</h3>

<p>Avoid mutable global state.</p>

<p><a id="s2.5.1-definition"></a>
<a id="251-definition"></a></p>

<p><a id="global-variables-definition"></a></p>
<h4 id="251-definition">2.5.1 Definition</h4>

<p>Module-level values or class attributes that can get mutated during program
execution.</p>

<p><a id="s2.5.2-pros"></a>
<a id="252-pros"></a></p>

<p><a id="global-variables-pros"></a></p>
<h4 id="252-pros">2.5.2 Pros</h4>

<p>Occasionally useful.</p>

<p><a id="s2.5.3-cons"></a>
<a id="253-cons"></a></p>

<p><a id="global-variables-cons"></a></p>
<h4 id="253-cons">2.5.3 Cons</h4>

<ul>
  <li>
    <p>Breaks encapsulation: Such design can make it hard to achieve valid
objectives. For example, if global state is used to manage a database
connection, then connecting to two different databases at the same time
(such as for computing differences during a migration) becomes difficult.
Similar problems easily arise with global registries.</p>
  </li>
  <li>
    <p>Has the potential to change module behavior during the import, because
assignments to global variables are done when the module is first imported.</p>
  </li>
</ul>

<p><a id="s2.5.4-decision"></a>
<a id="254-decision"></a></p>

<p><a id="global-variables-decision"></a></p>
<h4 id="254-decision">2.5.4 Decision</h4>

<p>Avoid mutable global state.</p>

<p>In those rare cases where using global state is warranted, mutable global
entities should be declared at the module level or as a class attribute and made
internal by prepending an <code class="language-plaintext highlighter-rouge">_</code> to the name. If necessary, external access to
mutable global state must be done through public functions or class methods. See
<a href="#s3.16-naming">Naming</a> below. Please explain the design reasons why mutable
global state is being used in a comment or a doc linked to from a comment.</p>

<p>Module-level constants are permitted and encouraged. For example:
<code class="language-plaintext highlighter-rouge">_MAX_HOLY_HANDGRENADE_COUNT = 3</code> for an internal use constant or
<code class="language-plaintext highlighter-rouge">SIR_LANCELOTS_FAVORITE_COLOR = "blue"</code> for a public API constant. Constants
must be named using all caps with underscores. See <a href="#s3.16-naming">Naming</a>
below.</p>

<p><a id="s2.6-nested"></a>
<a id="26-nested"></a></p>

<p><a id="nested-classes-functions"></a></p>
<h3 id="26-nestedlocalinner-classes-and-functions">2.6 Nested/Local/Inner Classes and Functions</h3>

<p>Nested local functions or classes are fine when used to close over a local
variable. Inner classes are fine.</p>

<p><a id="s2.6.1-definition"></a>
<a id="261-definition"></a></p>

<p><a id="nested-classes-functions-definition"></a></p>
<h4 id="261-definition">2.6.1 Definition</h4>

<p>A class can be defined inside of a method, function, or class. A function can be
defined inside a method or function. Nested functions have read-only access to
variables defined in enclosing scopes.</p>

<p><a id="s2.6.2-pros"></a>
<a id="262-pros"></a></p>

<p><a id="nested-classes-functions-pros"></a></p>
<h4 id="262-pros">2.6.2 Pros</h4>

<p>Allows definition of utility classes and functions that are only used inside of
a very limited scope. Very
<a href="https://en.wikipedia.org/wiki/Abstract_data_type">ADT</a>-y. Commonly used for
implementing decorators.</p>

<p><a id="s2.6.3-cons"></a>
<a id="263-cons"></a></p>

<p><a id="nested-classes-functions-cons"></a></p>
<h4 id="263-cons">2.6.3 Cons</h4>

<p>Nested functions and classes cannot be directly tested. Nesting can make the
outer function longer and less readable.</p>

<p><a id="s2.6.4-decision"></a>
<a id="264-decision"></a></p>

<p><a id="nested-classes-functions-decision"></a></p>
<h4 id="264-decision">2.6.4 Decision</h4>

<p>They are fine with some caveats. Avoid nested functions or classes except when
closing over a local value other than <code class="language-plaintext highlighter-rouge">self</code> or <code class="language-plaintext highlighter-rouge">cls</code>. Do not nest a function
just to hide it from users of a module. Instead, prefix its name with an _ at
the module level so that it can still be accessed by tests.</p>

<p><a id="s2.7-comprehensions"></a>
<a id="s2.7-list_comprehensions"></a>
<a id="27-list_comprehensions"></a>
<a id="list_comprehensions"></a>
<a id="list-comprehensions"></a></p>

<p><a id="comprehensions"></a></p>
<h3 id="27-comprehensions--generator-expressions">2.7 Comprehensions &amp; Generator Expressions</h3>

<p>Okay to use for simple cases.</p>

<p><a id="s2.7.1-definition"></a>
<a id="271-definition"></a></p>

<p><a id="comprehensions-definition"></a></p>
<h4 id="271-definition">2.7.1 Definition</h4>

<p>List, Dict, and Set comprehensions as well as generator expressions provide a
concise and efficient way to create container types and iterators without
resorting to the use of traditional loops, <code class="language-plaintext highlighter-rouge">map()</code>, <code class="language-plaintext highlighter-rouge">filter()</code>, or <code class="language-plaintext highlighter-rouge">lambda</code>.</p>

<p><a id="s2.7.2-pros"></a>
<a id="272-pros"></a></p>

<p><a id="comprehensions-pros"></a></p>
<h4 id="272-pros">2.7.2 Pros</h4>

<p>Simple comprehensions can be clearer and simpler than other dict, list, or set
creation techniques. Generator expressions can be very efficient, since they
avoid the creation of a list entirely.</p>

<p><a id="s2.7.3-cons"></a>
<a id="273-cons"></a></p>

<p><a id="comprehensions-cons"></a></p>
<h4 id="273-cons">2.7.3 Cons</h4>

<p>Complicated comprehensions or generator expressions can be hard to read.</p>

<p><a id="s2.7.4-decision"></a>
<a id="274-decision"></a></p>

<p><a id="comprehensions-decision"></a></p>
<h4 id="274-decision">2.7.4 Decision</h4>

<p>Comprehensions are allowed, however multiple <code class="language-plaintext highlighter-rouge">for</code> clauses or filter expressions
are not permitted. Optimize for readability, not conciseness.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">Yes</span><span class="p">:</span>
  <span class="n">result</span> <span class="o">=</span> <span class="p">[</span><span class="n">mapping_expr</span> <span class="k">for</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">iterable</span> <span class="k">if</span> <span class="n">filter_expr</span><span class="p">]</span>

  <span class="n">result</span> <span class="o">=</span> <span class="p">[</span>
      <span class="n">is_valid</span><span class="p">(</span><span class="n">metric</span><span class="o">=</span><span class="p">{</span><span class="s">'key'</span><span class="p">:</span> <span class="n">value</span><span class="p">})</span>
      <span class="k">for</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">interesting_iterable</span>
      <span class="k">if</span> <span class="n">a_longer_filter_expression</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
  <span class="p">]</span>

  <span class="n">descriptive_name</span> <span class="o">=</span> <span class="p">[</span>
      <span class="n">transform</span><span class="p">({</span><span class="s">'key'</span><span class="p">:</span> <span class="n">key</span><span class="p">,</span> <span class="s">'value'</span><span class="p">:</span> <span class="n">value</span><span class="p">},</span> <span class="n">color</span><span class="o">=</span><span class="s">'black'</span><span class="p">)</span>
      <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">generate_iterable</span><span class="p">(</span><span class="n">some_input</span><span class="p">)</span>
      <span class="k">if</span> <span class="n">complicated_condition_is_met</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
  <span class="p">]</span>

  <span class="n">result</span> <span class="o">=</span> <span class="p">[]</span>
  <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">y</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">):</span>
      <span class="k">if</span> <span class="n">x</span> <span class="o">*</span> <span class="n">y</span> <span class="o">&gt;</span> <span class="mi">10</span><span class="p">:</span>
        <span class="n">result</span><span class="p">.</span><span class="n">append</span><span class="p">((</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">))</span>

  <span class="k">return</span> <span class="p">{</span>
      <span class="n">x</span><span class="p">:</span> <span class="n">complicated_transform</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
      <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">long_generator_function</span><span class="p">(</span><span class="n">parameter</span><span class="p">)</span>
      <span class="k">if</span> <span class="n">x</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span>
  <span class="p">}</span>

  <span class="k">return</span> <span class="p">(</span><span class="n">x</span><span class="o">**</span><span class="mi">2</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>

  <span class="n">unique_names</span> <span class="o">=</span> <span class="p">{</span><span class="n">user</span><span class="p">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">user</span> <span class="ow">in</span> <span class="n">users</span> <span class="k">if</span> <span class="n">user</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">}</span>
</code></pre></div></div>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">No</span><span class="p">:</span>
  <span class="n">result</span> <span class="o">=</span> <span class="p">[(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span> <span class="k">for</span> <span class="n">y</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span> <span class="k">if</span> <span class="n">x</span> <span class="o">*</span> <span class="n">y</span> <span class="o">&gt;</span> <span class="mi">10</span><span class="p">]</span>

  <span class="k">return</span> <span class="p">(</span>
      <span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">z</span><span class="p">)</span>
      <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
      <span class="k">for</span> <span class="n">y</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
      <span class="k">if</span> <span class="n">x</span> <span class="o">!=</span> <span class="n">y</span>
      <span class="k">for</span> <span class="n">z</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
      <span class="k">if</span> <span class="n">y</span> <span class="o">!=</span> <span class="n">z</span>
  <span class="p">)</span>
</code></pre></div></div>

<p><a id="s2.8-default-iterators-and-operators"></a></p>

<p><a id="default-iterators-operators"></a></p>
<h3 id="28-default-iterators-and-operators">2.8 Default Iterators and Operators</h3>

<p>Use default iterators and operators for types that support them, like lists,
dictionaries, and files.</p>

<p><a id="s2.8.1-definition"></a>
<a id="281-definition"></a></p>

<p><a id="default-iterators-operators-definition"></a></p>
<h4 id="281-definition">2.8.1 Definition</h4>

<p>Container types, like dictionaries and lists, define default iterators and
membership test operators (“in” and “not in”).</p>

<p><a id="s2.8.2-pros"></a>
<a id="282-pros"></a></p>

<p><a id="default-iterators-operators-pros"></a></p>
<h4 id="282-pros">2.8.2 Pros</h4>

<p>The default iterators and operators are simple and efficient. They express the
operation directly, without extra method calls. A function that uses default
operators is generic. It can be used with any type that supports the operation.</p>

<p><a id="s2.8.3-cons"></a>
<a id="283-cons"></a></p>

<p><a id="default-iterators-operators-cons"></a></p>
<h4 id="283-cons">2.8.3 Cons</h4>

<p>You can’t tell the type of objects by reading the method names (unless the
variable has type annotations). This is also an advantage.</p>

<p><a id="s2.8.4-decision"></a>
<a id="284-decision"></a></p>

<p><a id="default-iterators-operators-decision"></a></p>
<h4 id="284-decision">2.8.4 Decision</h4>

<p>Use default iterators and operators for types that support them, like lists,
dictionaries, and files. The built-in types define iterator methods, too. Prefer
these methods to methods that return lists, except that you should not mutate a
container while iterating over it.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">Yes</span><span class="p">:</span>  <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">adict</span><span class="p">:</span> <span class="p">...</span>
      <span class="k">if</span> <span class="n">obj</span> <span class="ow">in</span> <span class="n">alist</span><span class="p">:</span> <span class="p">...</span>
      <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">afile</span><span class="p">:</span> <span class="p">...</span>
      <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">adict</span><span class="p">.</span><span class="n">items</span><span class="p">():</span> <span class="p">...</span>
</code></pre></div></div>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">No</span><span class="p">:</span>   <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">adict</span><span class="p">.</span><span class="n">keys</span><span class="p">():</span> <span class="p">...</span>
      <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span

