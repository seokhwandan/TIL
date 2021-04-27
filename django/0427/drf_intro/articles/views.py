# 윗줄은 django 모듈
from django.shortcuts import render, get_list_or_404, get_object_or_404

# 서드파티 앱 모듈 또는 파이썬모듈
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# 우리가 정의한 모듈
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    elif request.method == 'DELETE':
        article.delete()
        return Response({'id': article_pk}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail_update_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response({'id': comment_pk}, status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def index(request):
#     articles = get_list_or_404(Article)
#     serializer = ArticleListSerializer(articles, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def detail(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     serializer = ArticleListSerializer(article)
#     return Response(serializer.data)


# @api_view(['POST'])
# def create(request):

#     serializer = ArticleSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data, stauts=status.HTTP_201_CREATED)
    
#     # return Response(serializer.errors, stauts=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT'])
# def update(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)

#     serializer = ArticleSerializer(article, data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data)


# @api_view(['DELETE'])
# def delete(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     article.delete()
#     return Response({'id': article_pk}, status=status.HTTP_204_NO_CONTENT)