#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'foco_liao'

image_size = [1726, 972]

HD_size = [6465, 6465]

hd_arrow_1_path = '/images/HD_arrow-1.png'
img_arrow_1_path = '/images/img_arrow-1.png'
base_img_path = '/images/s2n_base_img.jpg'
hd_img_path = '/images/hd_img.png'
screen_path = '/images/screen.png'
edge_detection_save_directory = '/runs/edgeDetection/'
pre_segment_src_save_directory = '/runs/preSegmentSrc/'
pre_segment_src_pre = 'src_segment'
img_format = '.png'

pre_segment_dst_save_directory = '/runs/preSegmentDst/'
pre_segment_dst_pre = 'dst_segment'

step3_2_edge_image_path = '/images/step3-2_edge_image.jpg'

lookup_matrix_directory = '/runs/lookupMatrix/'

lookup_matrix_path = '/csvs/lookup_matrix.csv'

real_img_path = ['/images/s2n_identification-1.jpg',
                 '/images/s2n_identification-2.jpg',
                 '/images/s2n_identification-3.jpg',
                 '/images/s2n_identification-4.jpg',
                 '/images/s2n_identification-5.jpg',
                 '/images/s2n_identification-6.jpg',
                 '/images/s2n_identification-7.jpg',
                 '/images/s2n_identification-8.jpg',
                 '/images/s2n_identification-9.jpg',
                 '/images/s2n_identification-10.jpg']    #抖动图像的相对路径

real_time_img_path = ['/images/s2n_real_time_img.jpg']   #实时图像的相对路径


real_time_video_path = '/videos/s2n_detection_video.mp4'

box_save_track_path = '/csvs/box_track_data_image.csv' #识别后的车辆位置写回csv地址-box
box_save_trace_path = '/csvs/box_trace_data_video.csv' #识别后的车辆轨迹写回csv地址-box

seg_save_track_path = '/csvs/seg_track_data_image.csv' #识别后的车辆位置写回csv地址-segment
seg_save_trace_path = '/csvs/seg_trace_data_video.csv' #识别后的车辆轨迹写回csv地址-segment

flow_type = 'straight_flow' # 'straight_flow', 'turn_flow'

fusion_save_directory = '/images/fusion_result/' + flow_type + '/'

media_type = 0  # media_type: 0: image; 1: video
detection_type = 1   # detection_type: 0 ==> box;  1 ==> segment

video_rescale_x = 1920/3456
video_rescale_y = 1080/2234


#因为后续采用图片选点方式匹配，此部分配置信息可以不用了
src_match_shapes = [
              #人行横道
              #{'shape_id': 1,  'points_num': 4,'shape_style': 'polygon','points_coord':[(353,674),(385,675),(271,761),(234,760)]},
              #{'shape_id': 2,  'points_num': 4,'shape_style': 'polygon','points_coord':[(397,676),(430,676),(323,763),(285,762)]},
              {'shape_id': 3,  'points_num': 4,'shape_style': 'polygon','points_coord':[(441,677),(473,677),(374,765),(336,764)]},
              {'shape_id': 4,  'points_num': 4,'shape_style': 'polygon','points_coord':[(486,677),(518,678),(424,766),(387,765)]},
              #{'shape_id': 5,  'points_num': 4,'shape_style': 'polygon','points_coord':[(530,679),(565,679),(479,770),(440,768)]},
              {'shape_id': 6,  'points_num': 4,'shape_style': 'polygon','points_coord':[(577,680),(610,680),(531,771),(493,770)]},
              {'shape_id': 7,  'points_num': 4,'shape_style': 'polygon','points_coord':[(623,680),(657,681),(585,773),(544,772)]},
              {'shape_id': 8,  'points_num': 4,'shape_style': 'polygon','points_coord':[(670,682),(705,682),(639,775),(600,774)]},
              #{'shape_id': 9,  'points_num': 4,'shape_style': 'polygon','points_coord':[(717,683),(751,684),(694,777),(654,777)]},
              {'shape_id': 10, 'points_num': 4,'shape_style': 'polygon','points_coord':[(764,684),(799,685),(749,782),(710,779)]},
              #{'shape_id': 11, 'points_num': 4,'shape_style': 'polygon','points_coord':[(812,686),(847,688),(806,782),(765,781)]},
              {'shape_id': 12, 'points_num': 4,'shape_style': 'polygon','points_coord':[(860,688),(895,690),(863,786),(821,784)]},
              {'shape_id': 13, 'points_num': 4,'shape_style': 'polygon','points_coord':[(909,689),(946,690),(919,789),(878,787)]},
              {'shape_id': 14, 'points_num': 4,'shape_style': 'polygon','points_coord':[(959,691),(995,691),(975,790),(934,789)]},
              #{'shape_id': 15, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1008,692),(1044,693),(1031,793),(990,792)]},
              #{'shape_id': 16, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1056,694),(1093,695),(1088,796),(1046,794)]},
              #{'shape_id': 17, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1110,696),(1146,696),(1147,798),(1106,797)]},
              #{'shape_id': 18, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1161,697),(1198,697),(1205,802),(1163,799)]},
              #{'shape_id': 19, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1213,698),(1249,698),(1263,803),(1221,803)]},
              #{'shape_id': 20, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1266,700),(1303,700),(1326,805),(1283,805)]},
              #{'shape_id': 21, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1318,701),(1355,702),(1389,807),(1344,807)]},
              #{'shape_id': 22, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1372,703),(1411,704),(1450,808),(1406,808)]},
              #顶端三个
              {'shape_id': 23, 'points_num': 4,'shape_style': 'polygon','points_coord':[(459,577),(797,550),(794,553),(472,580)]},
              {'shape_id': 24, 'points_num': 4,'shape_style': 'polygon','points_coord':[(797,550),(812,558),(803,558),(794,553)]},
              {'shape_id': 25, 'points_num': 4,'shape_style': 'polygon','points_coord':[(459,577),(472,580),(475,583),(466,584)]},
              #最左待转道
              {'shape_id': 26, 'points_num': 4,'shape_style': 'polygon','points_coord':[(469,586),(478,585),(482,591),(473,591)]},
              {'shape_id': 27, 'points_num': 4,'shape_style': 'polygon','points_coord':[(476,595),(485,593),(488,599),(479,600)]},
              {'shape_id': 28, 'points_num': 4,'shape_style': 'polygon','points_coord':[(480,605),(489,605),(492,612),(482,613)]},
              {'shape_id': 29, 'points_num': 4,'shape_style': 'polygon','points_coord':[(481,617),(493,617),(493,625),(482,625)]},
              {'shape_id': 30, 'points_num': 4,'shape_style': 'polygon','points_coord':[(481,630),(492,630),(491,641),(480,641)]},
              #中间待转道
              {'shape_id': 31, 'points_num': 4,'shape_style': 'polygon','points_coord':[(629,566),(639,566),(649,572),(638,572)]},
              {'shape_id': 32, 'points_num': 4,'shape_style': 'polygon','points_coord':[(643,576),(653,575),(661,582),(650,582)]},
              {'shape_id': 33, 'points_num': 4,'shape_style': 'polygon','points_coord':[(658,588),(667,587),(674,595),(664,595)]},
              {'shape_id': 34, 'points_num': 4,'shape_style': 'polygon','points_coord':[(668,599),(677,598),(684,606),(674,607)]},
              {'shape_id': 35, 'points_num': 4,'shape_style': 'polygon','points_coord':[(678,613),(689,613),(694,622),(684,622)]},
              {'shape_id': 36, 'points_num': 4,'shape_style': 'polygon','points_coord':[(685,627),(696,627),(705,645),(694,645)]},
              #最右待转道
              {'shape_id': 37, 'points_num': 4,'shape_style': 'polygon','points_coord':[(810,561),(820,561),(831,568),(820,568)]},
              {'shape_id': 38, 'points_num': 4,'shape_style': 'polygon','points_coord':[(830,572),(840,572),(850,579),(840,579)]},
              {'shape_id': 39, 'points_num': 4,'shape_style': 'polygon','points_coord':[(850,584),(859,584),(870,592),(860,592)]},
              {'shape_id': 40, 'points_num': 4,'shape_style': 'polygon','points_coord':[(868,597),(877,597),(886,605),(876,605)]},
              {'shape_id': 41, 'points_num': 4,'shape_style': 'polygon','points_coord':[(883,611),(892,611),(902,620),(889,620)]},
              {'shape_id': 42, 'points_num': 4,'shape_style': 'polygon','points_coord':[(895,626),(906,626),(914,635),(902,635)]},
              {'shape_id': 43, 'points_num': 4,'shape_style': 'polygon','points_coord':[(907,642),(919,642),(925,651),(914,651)]}
              #左左转箭头
              #{'shape_id': 44, 'points_num': 3,'shape_style': 'polygon','points_coord':[(534,586),(541,578),(548,585)]},
              #{'shape_id': 45, 'points_num': 3,'shape_style': 'polygon','points_coord':[(534,586),(548,585),(555,590)]},
              #{'shape_id': 46, 'points_num': 3,'shape_style': 'polygon','points_coord':[(534,586),(555,590),(560,597)]},
              #{'shape_id': 47, 'points_num': 4,'shape_style': 'polygon','points_coord':[(548,585),(584,587),(580,592),(555,590)]},
              #{'shape_id': 48, 'points_num': 4,'shape_style': 'polygon','points_coord':[(584,587),(602,603),(592,603),(580,592)]},
              ##右左转箭头
              #{'shape_id': 49, 'points_num': 3,'shape_style': 'polygon','points_coord':[(706,572),(713,563),(734,581)]},
              #{'shape_id': 50, 'points_num': 4,'shape_style': 'polygon','points_coord':[(721,570),(759,572),(755,576),(727,575)]},
              #{'shape_id': 51, 'points_num': 4,'shape_style': 'polygon','points_coord':[(759,572),(782,588),(773,588),(755,576)]}
              ]
'''
src_unmatch_shapes = [     
              #人行横道    
              {'shape_id': 20000, 'points_num': 4,'shape_style': 'polygon','points_coord':[(473,677),(486,677),(387,765),(374,765)]},
              {'shape_id': 20001, 'points_num': 4,'shape_style': 'polygon','points_coord':[(518,678),(577,680),(493,770),(424,766)]},
              {'shape_id': 20002, 'points_num': 4,'shape_style': 'polygon','points_coord':[(610,680),(623,680),(544,772),(531,771)]},
              {'shape_id': 20003, 'points_num': 4,'shape_style': 'polygon','points_coord':[(657,681),(670,682),(600,774),(585,773)]},
              {'shape_id': 20004, 'points_num': 4,'shape_style': 'polygon','points_coord':[(705,682),(764,684),(710,779),(639,775)]},
              {'shape_id': 20005, 'points_num': 4,'shape_style': 'polygon','points_coord':[(799,685),(860,688),(821,784),(749,782)]},
              {'shape_id': 20006, 'points_num': 4,'shape_style': 'polygon','points_coord':[(895,690),(909,689),(878,787),(863,786)]},
              {'shape_id': 20007, 'points_num': 4,'shape_style': 'polygon','points_coord':[(946,690),(959,691),(934,789),(919,789)]},
              #人行横道与待转道之间
              {'shape_id': 20008, 'points_num': 4,'shape_style': 'polygon','points_coord':[(480,641),(491,641),(486,677),(473,677)]},
              {'shape_id': 20009, 'points_num': 4,'shape_style': 'polygon','points_coord':[(491,641),(694,645),(705,682),(486,677)]},
              {'shape_id': 20010, 'points_num': 4,'shape_style': 'polygon','points_coord':[(694,645),(705,645),(764,684),(705,682)]},
              {'shape_id': 20011, 'points_num': 4,'shape_style': 'polygon','points_coord':[(705,645),(914,651),(946,690),(764,684)]},
              {'shape_id': 20012, 'points_num': 4,'shape_style': 'polygon','points_coord':[(914,651),(925,651),(959,691),(946,690)]},
              
              
              #最左待转道之间:第一个特殊处理
              {'shape_id': 20013, 'points_num': 4,'shape_style': 'polygon','points_coord':[(466,584),(475,583),(478,585),(469,586)]},
              {'shape_id': 20014, 'points_num': 4,'shape_style': 'polygon','points_coord':[(473,591),(482,591),(485,593),(476,595)]},
              {'shape_id': 20015, 'points_num': 4,'shape_style': 'polygon','points_coord':[(479,600),(488,599),(489,605),(480,605)]},
              {'shape_id': 20016, 'points_num': 4,'shape_style': 'polygon','points_coord':[(482,613),(492,612),(493,617),(481,617)]},
              {'shape_id': 20017, 'points_num': 4,'shape_style': 'polygon','points_coord':[(482,625),(493,625),(492,630),(481,630)]},
              #中间待转道之间
              {'shape_id': 20018, 'points_num': 4,'shape_style': 'polygon','points_coord':[(638,572),(649,572),(653,575),(643,576)]},
              {'shape_id': 20019, 'points_num': 4,'shape_style': 'polygon','points_coord':[(650,582),(661,582),(667,587),(658,588)]},
              {'shape_id': 20020, 'points_num': 4,'shape_style': 'polygon','points_coord':[(664,595),(674,595),(677,598),(668,599)]},
              {'shape_id': 20021, 'points_num': 4,'shape_style': 'polygon','points_coord':[(674,607),(684,606),(689,613),(678,613)]},
              {'shape_id': 20022, 'points_num': 4,'shape_style': 'polygon','points_coord':[(684,622),(694,622),(696,627),(685,627)]},
              #最右待转道之间:第一个特殊处理
              {'shape_id': 20023, 'points_num': 4,'shape_style': 'polygon','points_coord':[(803,558),(812,558),(820,561),(810,561)]},
              {'shape_id': 20024, 'points_num': 4,'shape_style': 'polygon','points_coord':[(820,568),(831,568),(840,572),(830,572)]},
              {'shape_id': 20025, 'points_num': 4,'shape_style': 'polygon','points_coord':[(840,579),(850,579),(859,584),(850,584)]},
              {'shape_id': 20026, 'points_num': 4,'shape_style': 'polygon','points_coord':[(860,592),(870,592),(877,597),(868,597)]},
              {'shape_id': 20027, 'points_num': 4,'shape_style': 'polygon','points_coord':[(876,605),(886,605),(892,611),(883,611)]},
              {'shape_id': 20028, 'points_num': 4,'shape_style': 'polygon','points_coord':[(889,620),(902,620),(906,626),(895,626)]},
              {'shape_id': 20029, 'points_num': 4,'shape_style': 'polygon','points_coord':[(902,635),(914,635),(919,642),(907,642)]},
              #左待转道
              #（1）未匹配待转道小块之间横搭
              {'shape_id': 20030, 'points_num': 4,'shape_style': 'polygon','points_coord':[(475,583),(638,572),(643,576),(478,585)]},
              {'shape_id': 20031, 'points_num': 4,'shape_style': 'polygon','points_coord':[(482,591),(650,582),(658,588),(485,593)]},
              {'shape_id': 20032, 'points_num': 4,'shape_style': 'polygon','points_coord':[(488,599),(664,595),(668,599),(489,605)]},
              {'shape_id': 20033, 'points_num': 4,'shape_style': 'polygon','points_coord':[(492,612),(674,607),(678,613),(493,617)]},
              {'shape_id': 20034, 'points_num': 4,'shape_style': 'polygon','points_coord':[(493,625),(684,622),(685,627),(492,630)]},
              #（2）匹配待转道小块横搭
              {'shape_id': 20035, 'points_num': 4,'shape_style': 'polygon','points_coord':[(478,585),(643,576),(650,582),(482,591)]},
              {'shape_id': 20036, 'points_num': 4,'shape_style': 'polygon','points_coord':[(485,593),(658,588),(664,595),(488,599)]},
              {'shape_id': 20037, 'points_num': 4,'shape_style': 'polygon','points_coord':[(489,605),(668,599),(674,607),(492,612)]},
              {'shape_id': 20038, 'points_num': 4,'shape_style': 'polygon','points_coord':[(493,617),(678,613),(684,622),(493,625)]},
              {'shape_id': 20039, 'points_num': 4,'shape_style': 'polygon','points_coord':[(492,630),(685,627),(694,645),(491,641)]},
              #（3）最顶端那个横搭
              {'shape_id': 20040, 'points_num': 4,'shape_style': 'polygon','points_coord':[(472,580),(629,566),(638,572),(475,583)]},
              #右待转道
              #（1）未匹配待转道小块之间横搭:自上而下取5个
              {'shape_id': 20041, 'points_num': 4,'shape_style': 'polygon','points_coord':[(649,572),(803,558),(810,561),(653,575)]},
              {'shape_id': 20042, 'points_num': 4,'shape_style': 'polygon','points_coord':[(661,582),(820,568),(830,572),(667,587)]},
              {'shape_id': 20043, 'points_num': 4,'shape_style': 'polygon','points_coord':[(674,595),(840,579),(850,584),(677,598)]},
              {'shape_id': 20044, 'points_num': 4,'shape_style': 'polygon','points_coord':[(684,606),(860,592),(868,597),(689,613)]},
              {'shape_id': 20045, 'points_num': 4,'shape_style': 'polygon','points_coord':[(694,622),(876,605),(883,611),(696,627)]},
              #（2）匹配待转道小块横搭:自上而下取5个
              {'shape_id': 20046, 'points_num': 4,'shape_style': 'polygon','points_coord':[(639,566),(794,553),(803,558),(649,572)]},
              {'shape_id': 20047, 'points_num': 4,'shape_style': 'polygon','points_coord':[(653,575),(810,561),(820,568),(661,582)]},
              {'shape_id': 20048, 'points_num': 4,'shape_style': 'polygon','points_coord':[(667,587),(830,572),(840,579),(674,595)]},
              {'shape_id': 20049, 'points_num': 4,'shape_style': 'polygon','points_coord':[(677,598),(850,584),(860,592),(684,606)]},
              {'shape_id': 20050, 'points_num': 4,'shape_style': 'polygon','points_coord':[(689,613),(868,597),(876,605),(694,622)]},
              #（3）最底端那个横搭
              {'shape_id': 20051, 'points_num': 4,'shape_style': 'polygon','points_coord':[(696,627),(883,611),(914,651),(705,645)]}
              ]
'''

#由于不再继续采用坐标点匹配的方式，下面的src_unmatch_shapes不再使用
src_unmatch_shapes = [     
              #人行横道    
              {'shape_id': 20000, 'points_num': 4,'shape_style': 'polygon','points_coord':[(473,677),(486,677),(387,765),(374,765)]},
              {'shape_id': 20001, 'points_num': 4,'shape_style': 'polygon','points_coord':[(518,678),(577,680),(493,770),(424,766)]},
              {'shape_id': 20002, 'points_num': 4,'shape_style': 'polygon','points_coord':[(610,680),(623,680),(544,772),(531,771)]},
              {'shape_id': 20003, 'points_num': 4,'shape_style': 'polygon','points_coord':[(657,681),(670,682),(600,774),(585,773)]},
              {'shape_id': 20004, 'points_num': 4,'shape_style': 'polygon','points_coord':[(705,682),(764,684),(710,779),(639,775)]},
              {'shape_id': 20005, 'points_num': 4,'shape_style': 'polygon','points_coord':[(799,685),(860,688),(821,784),(749,782)]},
              {'shape_id': 20006, 'points_num': 4,'shape_style': 'polygon','points_coord':[(895,690),(909,689),(878,787),(863,786)]},
              {'shape_id': 20007, 'points_num': 4,'shape_style': 'polygon','points_coord':[(946,690),(959,691),(934,789),(919,789)]},
              #人行横道与待转道之间
              {'shape_id': 20008, 'points_num': 3,'shape_style': 'polygon','points_coord':[(480,641),(491,641),(486,677)]},
              {'shape_id': 20009, 'points_num': 3,'shape_style': 'polygon','points_coord':[(491,641),(694,645),(705,682)]},
              {'shape_id': 20010, 'points_num': 3,'shape_style': 'polygon','points_coord':[(694,645),(705,645),(764,684)]},
              {'shape_id': 20011, 'points_num': 3,'shape_style': 'polygon','points_coord':[(705,645),(914,651),(946,690)]},
              {'shape_id': 20012, 'points_num': 3,'shape_style': 'polygon','points_coord':[(914,651),(925,651),(959,691)]},

              {'shape_id': 20013, 'points_num': 3,'shape_style': 'polygon','points_coord':[(480,641),(486,677),(473,677)]},
              {'shape_id': 20014, 'points_num': 3,'shape_style': 'polygon','points_coord':[(491,641),(705,682),(486,677)]},
              {'shape_id': 20015, 'points_num': 3,'shape_style': 'polygon','points_coord':[(694,645),(764,684),(705,682)]},
              {'shape_id': 20016, 'points_num': 3,'shape_style': 'polygon','points_coord':[(705,645),(946,690),(764,684)]},
              {'shape_id': 20017, 'points_num': 3,'shape_style': 'polygon','points_coord':[(914,651),(959,691),(946,690)]},
              
              
              #最左待转道之间:第一个特殊处理
              {'shape_id': 20018, 'points_num': 4,'shape_style': 'polygon','points_coord':[(466,584),(475,583),(478,585),(469,586)]},
              {'shape_id': 20019, 'points_num': 4,'shape_style': 'polygon','points_coord':[(473,591),(482,591),(485,593),(476,595)]},
              {'shape_id': 20020, 'points_num': 4,'shape_style': 'polygon','points_coord':[(479,600),(488,599),(489,605),(480,605)]},
              {'shape_id': 20021, 'points_num': 4,'shape_style': 'polygon','points_coord':[(482,613),(492,612),(493,617),(481,617)]},
              {'shape_id': 20022, 'points_num': 4,'shape_style': 'polygon','points_coord':[(482,625),(493,625),(492,630),(481,630)]},
              #中间待转道之间
              {'shape_id': 20023, 'points_num': 4,'shape_style': 'polygon','points_coord':[(638,572),(649,572),(653,575),(643,576)]},
              {'shape_id': 20024, 'points_num': 4,'shape_style': 'polygon','points_coord':[(650,582),(661,582),(667,587),(658,588)]},
              {'shape_id': 20025, 'points_num': 4,'shape_style': 'polygon','points_coord':[(664,595),(674,595),(677,598),(668,599)]},
              {'shape_id': 20026, 'points_num': 4,'shape_style': 'polygon','points_coord':[(674,607),(684,606),(689,613),(678,613)]},
              {'shape_id': 20027, 'points_num': 4,'shape_style': 'polygon','points_coord':[(684,622),(694,622),(696,627),(685,627)]},
              #最右待转道之间:第一个特殊处理
              {'shape_id': 20028, 'points_num': 4,'shape_style': 'polygon','points_coord':[(803,558),(812,558),(820,561),(810,561)]},
              {'shape_id': 20029, 'points_num': 4,'shape_style': 'polygon','points_coord':[(820,568),(831,568),(840,572),(830,572)]},
              {'shape_id': 20030, 'points_num': 4,'shape_style': 'polygon','points_coord':[(840,579),(850,579),(859,584),(850,584)]},
              {'shape_id': 20031, 'points_num': 4,'shape_style': 'polygon','points_coord':[(860,592),(870,592),(877,597),(868,597)]},
              {'shape_id': 20032, 'points_num': 4,'shape_style': 'polygon','points_coord':[(876,605),(886,605),(892,611),(883,611)]},
              {'shape_id': 20033, 'points_num': 4,'shape_style': 'polygon','points_coord':[(889,620),(902,620),(906,626),(895,626)]},
              {'shape_id': 20034, 'points_num': 4,'shape_style': 'polygon','points_coord':[(902,635),(914,635),(919,642),(907,642)]},
              #左待转道
              #（1）未匹配待转道小块之间横搭
              {'shape_id': 20035, 'points_num': 3,'shape_style': 'polygon','points_coord':[(475,583),(638,572),(643,576)]},
              {'shape_id': 20036, 'points_num': 3,'shape_style': 'polygon','points_coord':[(482,591),(650,582),(658,588)]},
              {'shape_id': 20037, 'points_num': 3,'shape_style': 'polygon','points_coord':[(488,599),(664,595),(668,599)]},
              {'shape_id': 20038, 'points_num': 3,'shape_style': 'polygon','points_coord':[(492,612),(674,607),(678,613)]},
              {'shape_id': 20039, 'points_num': 3,'shape_style': 'polygon','points_coord':[(493,625),(684,622),(685,627)]},

              {'shape_id': 20040, 'points_num': 3,'shape_style': 'polygon','points_coord':[(475,583),(643,576),(478,585)]},
              {'shape_id': 20041, 'points_num': 3,'shape_style': 'polygon','points_coord':[(482,591),(658,588),(485,593)]},
              {'shape_id': 20042, 'points_num': 3,'shape_style': 'polygon','points_coord':[(488,599),(668,599),(489,605)]},
              {'shape_id': 20043, 'points_num': 3,'shape_style': 'polygon','points_coord':[(492,612),(678,613),(493,617)]},
              {'shape_id': 20044, 'points_num': 3,'shape_style': 'polygon','points_coord':[(493,625),(685,627),(492,630)]},
              #（2）匹配待转道小块横搭
              {'shape_id': 20045, 'points_num': 3,'shape_style': 'polygon','points_coord':[(478,585),(643,576),(650,582)]},
              {'shape_id': 20046, 'points_num': 3,'shape_style': 'polygon','points_coord':[(485,593),(658,588),(664,595)]},
              {'shape_id': 20047, 'points_num': 3,'shape_style': 'polygon','points_coord':[(489,605),(668,599),(674,607)]},
              {'shape_id': 20048, 'points_num': 3,'shape_style': 'polygon','points_coord':[(493,617),(678,613),(684,622)]},
              {'shape_id': 20049, 'points_num': 3,'shape_style': 'polygon','points_coord':[(492,630),(685,627),(694,645)]},

              {'shape_id': 20050, 'points_num': 3,'shape_style': 'polygon','points_coord':[(478,585),(650,582),(482,591)]},
              {'shape_id': 20051, 'points_num': 3,'shape_style': 'polygon','points_coord':[(485,593),(664,595),(488,599)]},
              {'shape_id': 20052, 'points_num': 3,'shape_style': 'polygon','points_coord':[(489,605),(674,607),(492,612)]},
              {'shape_id': 20053, 'points_num': 3,'shape_style': 'polygon','points_coord':[(493,617),(684,622),(493,625)]},
              {'shape_id': 20054, 'points_num': 3,'shape_style': 'polygon','points_coord':[(492,630),(694,645),(491,641)]},
              #（3）最顶端那个横搭
              {'shape_id': 20055, 'points_num': 3,'shape_style': 'polygon','points_coord':[(472,580),(629,566),(638,572)]},

              {'shape_id': 20056, 'points_num': 3,'shape_style': 'polygon','points_coord':[(472,580),(638,572),(475,583)]},
              #右待转道
              #（1）未匹配待转道小块之间横搭:自上而下取5个
              {'shape_id': 20057, 'points_num': 3,'shape_style': 'polygon','points_coord':[(649,572),(803,558),(810,561)]},
              {'shape_id': 20058, 'points_num': 3,'shape_style': 'polygon','points_coord':[(661,582),(820,568),(830,572)]},
              {'shape_id': 20059, 'points_num': 3,'shape_style': 'polygon','points_coord':[(674,595),(840,579),(850,584)]},
              {'shape_id': 20060, 'points_num': 3,'shape_style': 'polygon','points_coord':[(684,606),(860,592),(868,597)]},
              {'shape_id': 20061, 'points_num': 3,'shape_style': 'polygon','points_coord':[(694,622),(876,605),(883,611)]},

              {'shape_id': 20062, 'points_num': 3,'shape_style': 'polygon','points_coord':[(649,572),(810,561),(653,575)]},
              {'shape_id': 20063, 'points_num': 3,'shape_style': 'polygon','points_coord':[(661,582),(830,572),(667,587)]},
              {'shape_id': 20064, 'points_num': 3,'shape_style': 'polygon','points_coord':[(674,595),(850,584),(677,598)]},
              {'shape_id': 20065, 'points_num': 3,'shape_style': 'polygon','points_coord':[(684,606),(868,597),(689,613)]},
              {'shape_id': 20066, 'points_num': 3,'shape_style': 'polygon','points_coord':[(694,622),(883,611),(696,627)]},
              #（2）匹配待转道小块横搭:自上而下取5个
              {'shape_id': 20067, 'points_num': 3,'shape_style': 'polygon','points_coord':[(639,566),(794,553),(803,558)]},
              {'shape_id': 20068, 'points_num': 3,'shape_style': 'polygon','points_coord':[(653,575),(810,561),(820,568)]},
              {'shape_id': 20069, 'points_num': 3,'shape_style': 'polygon','points_coord':[(667,587),(830,572),(840,579)]},
              {'shape_id': 20070, 'points_num': 3,'shape_style': 'polygon','points_coord':[(677,598),(850,584),(860,592)]},
              {'shape_id': 20071, 'points_num': 3,'shape_style': 'polygon','points_coord':[(689,613),(868,597),(876,605)]},

              {'shape_id': 20072, 'points_num': 3,'shape_style': 'polygon','points_coord':[(639,566),(803,558),(649,572)]},
              {'shape_id': 20073, 'points_num': 3,'shape_style': 'polygon','points_coord':[(653,575),(820,568),(661,582)]},
              {'shape_id': 20074, 'points_num': 3,'shape_style': 'polygon','points_coord':[(667,587),(840,579),(674,595)]},
              {'shape_id': 20075, 'points_num': 3,'shape_style': 'polygon','points_coord':[(677,598),(860,592),(684,606)]},
              {'shape_id': 20076, 'points_num': 3,'shape_style': 'polygon','points_coord':[(689,613),(876,605),(694,622)]},
              #（3）最底端那个横搭
              {'shape_id': 20077, 'points_num': 3,'shape_style': 'polygon','points_coord':[(696,627),(883,611),(914,651)]},

              {'shape_id': 20078, 'points_num': 3,'shape_style': 'polygon','points_coord':[(696,627),(914,651),(705,645)]}
              ]


dst_match_shapes = [
              #人行横道
              {'shape_id': 10003,  'points_num': 4,'shape_style': 'polygon','points_coord':[(2194,1875),(2244,1863),(2387,2523),(2338,2534)]},
              {'shape_id': 10004,  'points_num': 4,'shape_style': 'polygon','points_coord':[(2300,1874),(2350,1863),(2503,2523),(2453,2534)]},
              {'shape_id': 10006,  'points_num': 4,'shape_style': 'polygon','points_coord':[(2450,1872),(2500,1862),(2638,2521),(2589,2532)]},
              {'shape_id': 10007,  'points_num': 4,'shape_style': 'polygon','points_coord':[(2562,1872),(2611,1860),(2755,2520),(2706,2531)]},
              {'shape_id': 10008,  'points_num': 4,'shape_style': 'polygon','points_coord':[(2683,1870),(2734,1858),(2877,2518),(2828,2530)]},
              {'shape_id': 10010, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2822,1868),(2872,1857),(3009,2517),(2958,2528)]},
              {'shape_id': 10012, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2925,1867),(2975,1855),(3127,2515),(3077,2527)]},
              {'shape_id': 10013, 'points_num': 4,'shape_style': 'polygon','points_coord':[(3057,1866),(3105,1854),(3260,2514),(3210,2525)]},
              {'shape_id': 10014, 'points_num': 4,'shape_style': 'polygon','points_coord':[(3173,1864),(3222,1853),(3376,2511),(3327,2523)]},
              #顶端三个
              {'shape_id': 10023, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1694,786),(2284,368),(2279,395),(1719,792)]},
              {'shape_id': 10024, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2284,368),(2346,460),(2330,470),(2279,395)]},
              {'shape_id': 10025, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1694,786),(1719,792),(1766,867),(1751,877)]},
              #最左待转道
              {'shape_id': 10026, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1793,943),(1808,933),(1850,999),(1835,1009)]},
              {'shape_id': 10027, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1876,1076),(1891,1067),(1932,1141),(1917,1151)]},
              {'shape_id': 10028, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1945,1203),(1961,1193),(1994,1253),(1978,1263)]},
              {'shape_id': 10029, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2008,1318),(2024,1308),(2056,1370),(2039,1378)]},
              {'shape_id': 10030, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2060,1426),(2077,1418),(2105,1481),(2088,1489)]},
              #中间待转道
              {'shape_id': 10031, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1974, 611),(1990, 600),(2037, 666),(2022, 677)]},
              {'shape_id': 10032, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2063, 742),(2078, 732),(2133, 820),(2118, 831)]},
              {'shape_id': 10033, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2165, 904),(2180, 894),(2224, 966),(2208, 977)]},
              {'shape_id': 10034, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2252,1049),(2267,1039),(2310,1110),(2295,1120)]},
              {'shape_id': 10035, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2331,1183),(2347,1173),(2394,1257),(2378,1267)]},
              {'shape_id': 10036, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2416,1338),(2432,1328),(2476,1410),(2460,1419)]},
              #最右待转道
              {'shape_id': 10037, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2361, 520),(2377, 510),(2424, 583),(2408, 594)]},
              {'shape_id': 10038, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2456, 671),(2472, 660),(2533, 758),(2517, 768)]},
              {'shape_id': 10039, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2547, 822),(2563, 812),(2605, 888),(2590, 897)]},
              {'shape_id': 10040, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2623, 958),(2639, 949),(2686,1032),(2670,1041)]},
              {'shape_id': 10041, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2706,1118),(2724,1109),(2766,1197),(2749,1206)]},
              {'shape_id': 10042, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2781,1272),(2799,1263),(2840,1349),(2822,1358)]},
              {'shape_id': 10043, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2861,1441),(2878,1433),(2915,1511),(2897,1519)]}
              ##左左转箭头
              #{'shape_id': 10044, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1897,958),(1833,795),(1889,880)]},
              #{'shape_id': 10045, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1897,958),(1889,880),(1946,966)]},
              #{'shape_id': 10046, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1897,958),(1946,966),(2000,1046)]},
              #{'shape_id': 10047, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1889,880),(2042,907),(2050,986),(1946,966)]},
              #{'shape_id': 10048, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2042,907),(2202,1148),(2171,1170),(2050,986)]},
              ##右左转箭头
              #{'shape_id': 10049, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2248,799),(2185,637),(2352,888)]},
              #{'shape_id': 10050, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2242,722),(2393,749),(2401,831),(2298,809)]},
              #{'shape_id': 10051, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2393,749),(2559,998),(2527,1019),(2401,831)]}
              ]
'''
dst_unmatch_shapes = [              
              #人行横道 
              {'shape_id': 30000, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2244,1863),(2300,1874),(2453,2534),(2387,2523)]},
              {'shape_id': 30001, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2350,1863),(2450,1872),(2589,2532),(2503,2523)]},
              {'shape_id': 30002, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2500,1862),(2562,1872),(2706,2531),(2638,2521)]},
              {'shape_id': 30003, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2611,1860),(2683,1870),(2828,2530),(2755,2520)]},
              {'shape_id': 30004, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2734,1858),(2822,1868),(2958,2528),(2877,2518)]},
              {'shape_id': 30005, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2872,1857),(2925,1867),(3077,2527),(3009,2517)]},
              {'shape_id': 30006, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2975,1855),(3057,1866),(3210,2525),(3127,2515)]},
              {'shape_id': 30007, 'points_num': 4,'shape_style': 'polygon','points_coord':[(3105,1854),(3173,1864),(3327,2523),(3260,2514)]},
              
              #人行横道与待转道之间
              {'shape_id': 30008, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2088,1489),(2105,1481),(2300,1874),(2244,1863)]},
              {'shape_id': 30009, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2105,1481),(2460,1419),(2734,1858),(2300,1874)]},
              {'shape_id': 30010, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2460,1419),(2476,1410),(2822,1868),(2734,1858)]},
              {'shape_id': 30011, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2476,1410),(2897,1519),(3105,1854),(2822,1868)]},
              {'shape_id': 30012, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2897,1519),(2915,1511),(3173,1864),(3105,1854)]},
              #最左待转道之间:第一个特殊处理
              {'shape_id': 30013, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1751, 877),(1766, 867),(1808, 933),(1793, 943)]},
              {'shape_id': 30014, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1835,1009),(1850, 999),(1891,1067),(1876,1076)]},
              {'shape_id': 30015, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1917,1151),(1932,1141),(1961,1193),(1945,1203)]},
              {'shape_id': 30016, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1978,1263),(1994,1253),(2024,1308),(2008,1318)]},
              {'shape_id': 30017, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2039,1378),(2056,1370),(2077,1418),(2060,1426)]},
              #中间待转道之间
              {'shape_id': 30018, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2022, 677),(2037, 666),(2078, 732),(2063, 742)]},
              {'shape_id': 30019, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2118, 831),(2133, 820),(2180, 894),(2165, 904)]},
              {'shape_id': 30020, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2208, 977),(2224, 966),(2267,1039),(2252,1049)]},
              {'shape_id': 30021, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2295,1120),(2310,1110),(2347,1173),(2331,1183)]},
              {'shape_id': 30022, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2378,1267),(2394,1257),(2432,1328),(2416,1338)]},
              #最右待转道之间:第一个特殊处理
              {'shape_id': 30023, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2330, 470),(2346, 460),(2377, 510),(2361, 520)]},
              {'shape_id': 30024, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2408, 594),(2424, 583),(2472, 660),(2456, 671)]},
              {'shape_id': 30025, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2517, 768),(2533, 758),(2563, 812),(2547, 822)]},
              {'shape_id': 30026, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2590, 897),(2605, 888),(2639, 949),(2623, 958)]},
              {'shape_id': 30027, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2670,1041),(2686,1032),(2724,1109),(2706,1118)]},
              {'shape_id': 30028, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2749,1206),(2766,1197),(2799,1263),(2781,1272)]},
              {'shape_id': 30029, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2822,1358),(2840,1349),(2878,1433),(2861,1441)]},

              #左待转道
              #（1）未匹配待转道小块之间横搭
              {'shape_id': 30030, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1766, 867),(2022, 677),(2063, 742),(1808, 933)]},
              {'shape_id': 30031, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1850, 999),(2118, 831),(2165, 904),(1891,1067)]},
              {'shape_id': 30032, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1932,1141),(2208, 977),(2252,1049),(1961,1193)]},
              {'shape_id': 30033, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1994,1253),(2295,1120),(2331,1183),(2024,1308)]},
              {'shape_id': 30034, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2056,1370),(2378,1267),(2416,1338),(2077,1418)]},
              #（2）匹配待转道小块横搭
              {'shape_id': 30035, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1808, 933),(2063, 742),(2118, 831),(1850, 999)]},
              {'shape_id': 30036, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1891,1067),(2165, 904),(2208, 977),(1932,1141)]},
              {'shape_id': 30037, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1961,1193),(2252,1049),(2295,1120),(1994,1253)]},
              {'shape_id': 30038, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2024,1308),(2331,1183),(2378,1267),(2056,1370)]},
              {'shape_id': 30039, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2077,1418),(2416,1338),(2460,1419),(2105,1481)]},
              #（3）最顶端那个横搭
              {'shape_id': 30040, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1719, 792),(1974, 611),(2022, 677),(1766, 867)]},
              #右待转道
              #（1）未匹配待转道小块之间横搭:自上而下取5个
              {'shape_id': 30041, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2037, 666),(2330, 470),(2361, 520),(2078, 732)]},
              {'shape_id': 30042, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2133, 820),(2408, 594),(2456, 671),(2180, 894)]},
              {'shape_id': 30043, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2224, 966),(2517, 768),(2547, 822),(2267,1039)]},
              {'shape_id': 30044, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2310,1110),(2590, 897),(2623, 958),(2347,1173)]},
              {'shape_id': 30045, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2394,1257),(2670,1041),(2706,1118),(2432,1328)]},
              #（2）匹配待转道小块横搭:自上而下取5个
              {'shape_id': 30046, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1990, 600),(2279, 395),(2330, 470),(2037, 666)]},
              {'shape_id': 30047, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2078, 732),(2361, 520),(2408, 594),(2133, 820)]},
              {'shape_id': 30048, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2180, 894),(2456, 671),(2517, 768),(2224, 966)]},
              {'shape_id': 30049, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2267,1039),(2547, 822),(2590, 897),(2310,1110)]},
              {'shape_id': 30050, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2347,1173),(2623, 958),(2670,1041),(2394,1257)]},
              #（3）最底端那个横搭
              {'shape_id': 30051, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2432,1328),(2706,1118),(2897,1519),(2476,1410)]}
              ]
'''
dst_unmatch_shapes = [              
              #人行横道 
              {'shape_id': 30000, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2244,1863),(2300,1874),(2453,2534),(2387,2523)]},
              {'shape_id': 30001, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2350,1863),(2450,1872),(2589,2532),(2503,2523)]},
              {'shape_id': 30002, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2500,1862),(2562,1872),(2706,2531),(2638,2521)]},
              {'shape_id': 30003, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2611,1860),(2683,1870),(2828,2530),(2755,2520)]},
              {'shape_id': 30004, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2734,1858),(2822,1868),(2958,2528),(2877,2518)]},
              {'shape_id': 30005, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2872,1857),(2925,1867),(3077,2527),(3009,2517)]},
              {'shape_id': 30006, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2975,1855),(3057,1866),(3210,2525),(3127,2515)]},
              {'shape_id': 30007, 'points_num': 4,'shape_style': 'polygon','points_coord':[(3105,1854),(3173,1864),(3327,2523),(3260,2514)]},
              
              #人行横道与待转道之间
              {'shape_id': 30008, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2088,1489),(2105,1481),(2300,1874)]},
              {'shape_id': 30009, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2105,1481),(2460,1419),(2734,1858)]},
              {'shape_id': 30010, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2460,1419),(2476,1410),(2822,1868)]},
              {'shape_id': 30011, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2476,1410),(2897,1519),(3105,1854)]},
              {'shape_id': 30012, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2897,1519),(2915,1511),(3173,1864)]},

              {'shape_id': 30013, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2088,1489),(2300,1874),(2244,1863)]},
              {'shape_id': 30014, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2105,1481),(2734,1858),(2300,1874)]},
              {'shape_id': 30015, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2460,1419),(2822,1868),(2734,1858)]},
              {'shape_id': 30016, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2476,1410),(3105,1854),(2822,1868)]},
              {'shape_id': 30017, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2897,1519),(3173,1864),(3105,1854)]},
              #最左待转道之间:第一个特殊处理
              {'shape_id': 30018, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1751, 877),(1766, 867),(1808, 933),(1793, 943)]},
              {'shape_id': 30019, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1835,1009),(1850, 999),(1891,1067),(1876,1076)]},
              {'shape_id': 30020, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1917,1151),(1932,1141),(1961,1193),(1945,1203)]},
              {'shape_id': 30021, 'points_num': 4,'shape_style': 'polygon','points_coord':[(1978,1263),(1994,1253),(2024,1308),(2008,1318)]},
              {'shape_id': 30022, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2039,1378),(2056,1370),(2077,1418),(2060,1426)]},
              #中间待转道之间
              {'shape_id': 30023, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2022, 677),(2037, 666),(2078, 732),(2063, 742)]},
              {'shape_id': 30024, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2118, 831),(2133, 820),(2180, 894),(2165, 904)]},
              {'shape_id': 30025, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2208, 977),(2224, 966),(2267,1039),(2252,1049)]},
              {'shape_id': 30026, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2295,1120),(2310,1110),(2347,1173),(2331,1183)]},
              {'shape_id': 30027, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2378,1267),(2394,1257),(2432,1328),(2416,1338)]},
              #最右待转道之间:第一个特殊处理
              {'shape_id': 30028, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2330, 470),(2346, 460),(2377, 510),(2361, 520)]},
              {'shape_id': 30029, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2408, 594),(2424, 583),(2472, 660),(2456, 671)]},
              {'shape_id': 30030, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2517, 768),(2533, 758),(2563, 812),(2547, 822)]},
              {'shape_id': 30031, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2590, 897),(2605, 888),(2639, 949),(2623, 958)]},
              {'shape_id': 30032, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2670,1041),(2686,1032),(2724,1109),(2706,1118)]},
              {'shape_id': 30033, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2749,1206),(2766,1197),(2799,1263),(2781,1272)]},
              {'shape_id': 30034, 'points_num': 4,'shape_style': 'polygon','points_coord':[(2822,1358),(2840,1349),(2878,1433),(2861,1441)]},

              #左待转道
              #（1）未匹配待转道小块之间横搭
              {'shape_id': 30035, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1766, 867),(2022, 677),(2063, 742)]},
              {'shape_id': 30036, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1850, 999),(2118, 831),(2165, 904)]},
              {'shape_id': 30037, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1932,1141),(2208, 977),(2252,1049)]},
              {'shape_id': 30038, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1994,1253),(2295,1120),(2331,1183)]},
              {'shape_id': 30039, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2056,1370),(2378,1267),(2416,1338)]},

              {'shape_id': 30040, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1766, 867),(2063, 742),(1808, 933)]},
              {'shape_id': 30041, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1850, 999),(2165, 904),(1891,1067)]},
              {'shape_id': 30042, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1932,1141),(2252,1049),(1961,1193)]},
              {'shape_id': 30043, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1994,1253),(2331,1183),(2024,1308)]},
              {'shape_id': 30044, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2056,1370),(2416,1338),(2077,1418)]},
              #（2）匹配待转道小块横搭
              {'shape_id': 30045, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1808, 933),(2063, 742),(2118, 831)]},
              {'shape_id': 30046, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1891,1067),(2165, 904),(2208, 977)]},
              {'shape_id': 30047, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1961,1193),(2252,1049),(2295,1120)]},
              {'shape_id': 30048, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2024,1308),(2331,1183),(2378,1267)]},
              {'shape_id': 30049, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2077,1418),(2416,1338),(2460,1419)]},

              {'shape_id': 30050, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1808, 933),(2118, 831),(1850, 999)]},
              {'shape_id': 30051, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1891,1067),(2208, 977),(1932,1141)]},
              {'shape_id': 30052, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1961,1193),(2295,1120),(1994,1253)]},
              {'shape_id': 30053, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2024,1308),(2378,1267),(2056,1370)]},
              {'shape_id': 30054, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2077,1418),(2460,1419),(2105,1481)]},
              #（3）最顶端那个横搭
              {'shape_id': 30055, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1719, 792),(1974, 611),(2022, 677)]},

              {'shape_id': 30056, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1719, 792),(2022, 677),(1766, 867)]},
              #右待转道
              #（1）未匹配待转道小块之间横搭:自上而下取5个
              {'shape_id': 30057, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2037, 666),(2330, 470),(2361, 520)]},
              {'shape_id': 30058, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2133, 820),(2408, 594),(2456, 671)]},
              {'shape_id': 30059, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2224, 966),(2517, 768),(2547, 822)]},
              {'shape_id': 30060, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2310,1110),(2590, 897),(2623, 958)]},
              {'shape_id': 30061, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2394,1257),(2670,1041),(2706,1118)]},

              {'shape_id': 30062, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2037, 666),(2361, 520),(2078, 732)]},
              {'shape_id': 30063, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2133, 820),(2456, 671),(2180, 894)]},
              {'shape_id': 30064, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2224, 966),(2547, 822),(2267,1039)]},
              {'shape_id': 30065, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2310,1110),(2623, 958),(2347,1173)]},
              {'shape_id': 30066, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2394,1257),(2706,1118),(2432,1328)]},
              #（2）匹配待转道小块横搭:自上而下取5个
              {'shape_id': 30067, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1990, 600),(2279, 395),(2330, 470)]},
              {'shape_id': 30068, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2078, 732),(2361, 520),(2408, 594)]},
              {'shape_id': 30069, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2180, 894),(2456, 671),(2517, 768)]},
              {'shape_id': 30070, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2267,1039),(2547, 822),(2590, 897)]},
              {'shape_id': 30071, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2347,1173),(2623, 958),(2670,1041)]},

              {'shape_id': 30072, 'points_num': 3,'shape_style': 'polygon','points_coord':[(1990, 600),(2330, 470),(2037, 666)]},
              {'shape_id': 30073, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2078, 732),(2408, 594),(2133, 820)]},
              {'shape_id': 30074, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2180, 894),(2517, 768),(2224, 966)]},
              {'shape_id': 30075, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2267,1039),(2590, 897),(2310,1110)]},
              {'shape_id': 30076, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2347,1173),(2670,1041),(2394,1257)]},
              #（3）最底端那个横搭
              {'shape_id': 30077, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2432,1328),(2706,1118),(2897,1519)]},

              {'shape_id': 30078, 'points_num': 3,'shape_style': 'polygon','points_coord':[(2432,1328),(2897,1519),(2476,1410)]}
              ]


