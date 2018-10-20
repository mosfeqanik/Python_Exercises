import re
st=""" <<div class="book-cover">

					 <a href="http://dimik.pub/book/357/machine-learning-algorithm-by-nafis-neehal"><img src="http://dimik.pub/wp-content/uploads/2018/09/42655899_2008793782745518_1418741273983975424_n.jpg"></a>
                </div><!-- end .book-cover -->



                <div class="slide-description">

                    <div class="inner-sd">

                        <div class="top-sd-head clearfix">

                            <div class="tsh-left">

                            <h2 class="sd-title"><a href="http://dimik.pub/book/357/machine-learning-algorithm-by-nafis-neehal">মেশিন লার্নিং অ‍্যালগরিদম</a></h2>"""
regexp=re.compile(r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)">.*?<h2 class="sd-title"><.*?>(.*?)<',re.S)

result=re.findall(regexp,st)
print(result)