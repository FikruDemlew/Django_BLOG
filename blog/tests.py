from django.test import TestCase
from django.urls import reverse

from .models import Blog


class BlogEditDeleteTests(TestCase):
    def setUp(self):
        self.blog = Blog.objects.create(
            title='Original title',
            content='Original content',
            isPublished=False,
        )

    def test_can_edit_blog_from_edit_page_and_redirect_to_detail(self):
        response = self.client.post(
            reverse('blog_edit', args=[self.blog.id]),
            {
                'title': 'Updated title',
                'content': 'Updated content',
                'isPublished': 'on',
            },
            follow=True,
        )

        self.assertRedirects(response, reverse('blog_detail', args=[self.blog.id]))
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.title, 'Updated title')
        self.assertEqual(self.blog.content, 'Updated content')
        self.assertTrue(self.blog.isPublished)

    def test_can_create_blog_and_redirect_to_detail(self):
        response = self.client.post(
            reverse('blog_create'),
            {
                'title': 'New blog title',
                'content': 'New blog content',
                'isPublished': 'on',
            },
            follow=True,
        )

        created_blog = Blog.objects.get(title='New blog title')
        self.assertRedirects(response, reverse('blog_detail', args=[created_blog.id]))
        self.assertTrue(Blog.objects.filter(title='New blog title').exists())

    def test_can_delete_blog(self):
        response = self.client.post(reverse('delete_blog', args=[self.blog.id]), follow=True)

        self.assertRedirects(response, reverse('blog_index'))
        self.assertFalse(Blog.objects.filter(id=self.blog.id).exists())
