"""
!/usr/bin/env python
 -*- coding: utf-8 -*-
 @CreateTime    : 2024-09-27 16:34
 @Author  : Ivan Mao
 @File    : test.py.py
 @Description : 
"""


def get_private_image(compute, project, family):
    try:
        image = compute.images().getFromFamily(
            project=project,
            family=family
        ).execute()
        print(f"找到镜像: {image['name']}")
        print(f"镜像链接: {image['selfLink']}")
        return image
    except Exception as e:
        print(f"无法找到镜像: {e}")
        return None

def list_private_images(compute, project):
    try:
        images = compute.images().list(project=project).execute()
        if 'items' in images:
            for img in images['items']:
                print(f"镜像名称: {img['name']}, 链接: {img['selfLink']}")
                print(img)
        else:
            print("没有找到镜像。")
    except Exception as e:
        print(f"无法列出镜像: {e}")

if __name__ == '__main__':
    import googleapiclient.discovery
    # 创建compute服务
    compute = googleapiclient.discovery.build('compute', 'v1')
    # image_project = 'cuda-cl'
    image_family = 'e4750-env'
    image_project = 'heterogeneous-computing-435900'

    # image = get_private_image(compute, image_project, image_family)
    # list_private_images(compute, image_project)
    image = get_private_image(compute, image_project, image_family)