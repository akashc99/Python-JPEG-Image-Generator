<h1>Python Image Generator</h1>
<p>This program generates an image with a user-specified file size in megabytes. The image is created by filling it with random pixel values.</p>
<h2>Prerequisites</h2>
<ul>
  <li>Python 3</li>
</ul>
<h2>Usage</h2>
<pre><code>python image_generator.py --size SIZE
</code></pre>
<p>Replace <code>SIZE</code> with the desired size of the image in megabytes. For example, to generate an image with a file size of 1 MB, you would run the following command:</p>
<pre><code>python image_generator.py --size 1
</code></pre>
<p>The program will generate an image file with the specified file size and print the actual file size of the generated image to the console. The generated image will be saved in the same directory as the program file with a file name in the format <code>SIZEmb.jpg</code>, where <code>SIZE</code> is the specified size of the image.</p>
<h2>Example</h2>
<p>To generate an image with a file size of 2 MB:</p>
<pre><code>python image_generator.py --size 2
</code></pre>
<p>This will generate an image file with a file name of <code>2mb.jpg</code> and a file size of approximately 2 MB. The actual file size may vary slightly due to the random nature of the pixel values.</p>
<h2>Note</h2>
<p>The program may take a few seconds to generate the image, depending on the size of the image and the performance of your system.</p>
<h2>Credits</h2>
<p>chagpt</p>
<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
