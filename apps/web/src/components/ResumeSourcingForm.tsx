import React, { useState } from 'react';

export function ResumeSourcingForm({ onScreen }: { onScreen: (res: any) => void }) {
  const [name, setName] = useState('Abebe Bikila');
  const [skills, setSkills] = useState('Python, FastAPI, React, PyTorch, SQL');
  const [experience, setExperience] = useState(4.5);

  const handleScreen = (e: React.FormEvent) => {
    e.preventDefault();
    const skillList = skills.split(',').map(s => s.trim());
    const required = ['Python', 'FastAPI', 'React', 'PyTorch'];
    const matched = skillList.filter(s => required.includes(s));
    const score = Math.round((matched.length / required.length) * 80 + Math.min(experience, 5) * 4);

    onScreen({
      candidateName: name,
      matchScore: score,
      matchedSkills: matched,
      status: score >= 75 ? 'RECOMMENDED' : 'REVIEW_NEEDED',
      generatedQuestions: [
        'How do you manage async context in FastAPI dependency injection?',
        'Describe state management in React 18 using hooks vs Zustand.'
      ]
    });
  };

  return (
    <form onSubmit={handleScreen} style={{ background: '#ffffff', padding: '1.5rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
      <h3 style={{ color: '#0f172a', marginBottom: '1rem' }}>📄 AI Resume Parsing & Skill Matcher</h3>
      <div style={{ display: 'grid', gap: '1rem', gridTemplateColumns: '1fr 1fr' }}>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Candidate Name</label>
          <input value={name} onChange={e => setName(e.target.value)} style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Years of Experience</label>
          <input type="number" step="0.5" value={experience} onChange={e => setExperience(Number(e.target.value))} style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
      </div>
      <div style={{ marginTop: '1rem' }}>
        <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Parsed Skills (Comma-separated)</label>
        <input value={skills} onChange={e => setSkills(e.target.value)} style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
      </div>
      <button type="submit" style={{ marginTop: '1rem', background: '#0d9488', color: '#fff', padding: '0.75rem 1.5rem', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}>
        Compute Skill Match Score
      </button>
    </form>
  );
}
