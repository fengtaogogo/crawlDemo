import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem


class ImgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_url'])

    def item_completed(self, results, item, info):
        image_url = [x['path'] for ok, x in results if ok]

        if not image_url:
            raise DropItem("Item contains no images")

        item['img_url'] = image_url
        return item
