// Recomendações de canais e livros baseadas na emoção 
const recommendations = {
    ansioso: {
      videos: [
        { name: 'Técnica de Respiração', link: '#tecnica-de-respiracao' },
        { name: 'Relaxamento Muscular Progressivo', link: '#relaxamento-muscular-progressivo' }
      ],
      canais: [
        { name: 'Saúde da Mente', url: 'https://www.youtube.com/@saudedamente1548', description: 'O canal "Saúde da Mente", apresentado pelo Dr. Marco Abud, oferece conteúdos valiosos sobre saúde mental, bem-estar e técnicas para gerenciar a ansiedade e o estresse.' },
        { name: 'Casule', url: 'https://www.youtube.com/@casule', description: 'O canal Casule traz uma abordagem diferenciada para o bem-estar mental, explorando temas de meditação, práticas de mindfulness e muito mais.' }
      ],
      livros: [
        { 
          title: 'Coisas que Você Só Descobre Quando Desacelera', 
          description: 'Este livro, escrito por Haemin Sunim, aborda como desacelerar e refletir sobre a vida em meio à correria do cotidiano. Ele oferece insights profundos para viver de forma mais consciente e atenta.', 
          link: 'https://www.amazon.com.br/coisas-que-você-quando-desacelera/dp/8543105293', 
          author: 'Haemin Sunim', 
          publisher: 'Editora Leya' 
        }
      ]
    },
    estressado: {
      videos: [
        { name: 'Técnica do Mergulho', link: '#tecnica-do-mergulho' },
        { name: 'Visualização Positiva', link: '#visualizacao-positiva' }
      ],
      canais: [
        { name: 'Saúde da Mente', url: 'https://www.youtube.com/@saudedamente1548', description: 'O canal "Saúde da Mente", apresentado pelo Dr. Marco Abud, oferece conteúdos valiosos sobre saúde mental, bem-estar e técnicas para gerenciar a ansiedade e o estresse.' },
        { name: 'Casule', url: 'https://www.youtube.com/@casule', description: 'O canal Casule traz uma abordagem diferenciada para o bem-estar mental, explorando temas de meditação, práticas de mindfulness e muito mais.' }
      ],
      livros: [
        { 
          title: 'Desconstruindo a Ansiedade', 
          description: 'Este livro oferece estratégias práticas para lidar com a ansiedade no dia a dia, com técnicas baseadas em mindfulness e psicologia cognitiva comportamental (TCC).', 
          link: 'https://www.amazon.com.br/Desconstruindo-ansiedade-superar-agitação-preocupação/dp/6555642505', 
          author: 'Dr. Arthur R. B. Costa', 
          publisher: 'Editora Gente'
        }
      ]
    },
    calmo: {
      videos: [
        { name: 'Técnica de Respiração', link: '#tecnica-de-respiracao' },
        { name: 'Relaxamento Muscular Progressivo', link: '#relaxamento-muscular-progressivo' }
      ],
      canais: [
        { name: 'Saúde da Mente', url: 'https://www.youtube.com/@saudedamente1548', description: 'O canal "Saúde da Mente", apresentado pelo Dr. Marco Abud, oferece conteúdos valiosos sobre saúde mental, bem-estar e técnicas para gerenciar a ansiedade e o estresse.' },
        { name: 'Casule', url: 'https://www.youtube.com/@casule', description: 'O canal Casule traz uma abordagem diferenciada para o bem-estar mental, explorando temas de meditação, práticas de mindfulness e muito mais.' }
      ],
      livros: [
        { 
          title: 'A Voz da Sua Cabeça', 
          description: 'Este livro foca em como controlar os pensamentos negativos que geram ansiedade, agitação e estresse. Oferece ferramentas para mudar a forma como lidamos com esses pensamentos automáticos.', 
          link: 'https://www.amazon.com.br/voz-sua-cabeça-reduzir-transformar/dp/6555641843', 
          author: 'Dr. David Carbonell', 
          publisher: 'Editora Vozes'
        }
      ]
    }
  };
  
  document.getElementById('recommend-button').addEventListener('click', () => {
    const emotion = document.getElementById('emotion').value;
    const container = document.getElementById('recommendation-container');
    container.innerHTML = ''; 
  
    const userRecommendations = recommendations[emotion];
  
    // Exibe as técnicas de vídeo recomendadas
    userRecommendations.videos.forEach(video => {
      const videoCard = document.createElement('div');
      videoCard.className = 'recommendation';  
  
      const title = document.createElement('h5');
      title.textContent = video.name;
  
      const link = document.createElement('a');
      link.href = video.link;
      link.textContent = 'Saiba mais';
      link.className = 'btn-primary';
  
      videoCard.appendChild(title);
      videoCard.appendChild(link);
      container.appendChild(videoCard);
    });
  
    // Exibe canais no YouTube
    userRecommendations.canais.forEach(channel => {
      const channelCard = document.createElement('div');
      channelCard.className = 'recommendation';  
  
      const title = document.createElement('h5');
      title.textContent = channel.name;
  
      const description = document.createElement('p');
      description.textContent = channel.description;
  
      const link = document.createElement('a');
      link.href = channel.url;
      link.target = '_blank';
      link.textContent = 'Acesse o canal';
      link.className = 'btn-primary';
  
      channelCard.appendChild(title);
      channelCard.appendChild(description);
      channelCard.appendChild(link);
      container.appendChild(channelCard);
    });
  
    // Exibe livros
    userRecommendations.livros.forEach(book => {
      const bookCard = document.createElement('div');
      bookCard.className = 'recommendation';  
  
      const title = document.createElement('h5');
      title.textContent = book.title;
  
      const description = document.createElement('p');
      description.textContent = book.description;
  
      const author = document.createElement('p');
      author.textContent = `Autor: ${book.author}`;
  
      const publisher = document.createElement('p');
      publisher.textContent = `Editor: ${book.publisher}`;
  
      const link = document.createElement('a');
      link.href = book.link;
      link.target = '_blank';
      link.textContent = 'Comprar no Amazon';
      link.className = 'btn-primary';
  
      bookCard.appendChild(title);
      bookCard.appendChild(description);
      bookCard.appendChild(author);
      bookCard.appendChild(publisher);
      bookCard.appendChild(link);
      container.appendChild(bookCard);
    });
  
    // Adiciona animação de fade-in nas recomendações
    container.classList.add('fade-in');
    setTimeout(() => {
      container.classList.remove('fade-in');
    }, 600); // Tempo da animação
  });
  
