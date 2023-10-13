from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import IndexView, ProdutoView, CarrinhoComprasView, LoginView, PerfilView, PedidoView, \
PagamentoView

router = SimpleRouter()
router.register('produto', ProdutoView)
router.register('carrinho-de-compras', CarrinhoComprasView)
router.register('login', LoginView)
router.register('perfil', PerfilView)
router.register('pedido', PedidoView)
router.register('pagamento', PagamentoView)

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('produto/', ProdutoView.as_view(), name='produto'),
    path('carrinho-de-compras/', CarrinhoComprasView.as_view(), name="carrinho-de-compras"),
    path('login/', LoginView.as_view(), name="login"),
    path('perfil/', PerfilView.as_view(), name="perfil"),
    path('pedido/', PedidoView.as_view(), name="pedido"),
    path('pagamento/', PagamentoView.as_view(), name="pagamento"),
]
