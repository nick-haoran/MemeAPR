from cnstd import CnStd
from cnocr import CnOcr
 
std = CnStd()
cn_ocr = CnOcr()
 
box_infos = std.detect('test.png', resized_shape=(768, 1024))
 
print(len(box_infos['detected_texts']))
for box_info in box_infos['detected_texts']:
    cropped_img = box_info['cropped_img']
    ocr_res = cn_ocr.ocr_for_single_line(cropped_img)
    print('ocr result: %s' % str(ocr_res))